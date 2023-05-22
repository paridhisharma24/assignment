from model.report import report
from model.store_status import store_status
from model.menu_hours import menu_hours
from model.bq_results import bq_results
from connect import db
import string
import random

import datetime
import pytz 

current_date = datetime_object = datetime.datetime.strptime('25-01-2023 00:00:00', '%d-%m-%Y %H:%M:%S')
one_week_before = current_date - datetime.timedelta(days=7)

def generate_report():
    report_id = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=10))
    
    stores = [x[0] for x in db.session.query(menu_hours.store_id).distinct()]
    
    for store_id in stores:
        tz = db.session.query(bq_results.timezone_str).filter(bq_results.store_id == store_id)

        if tz.count() == 0:
            tz = 'America/Chicago'

        time_zone = pytz.timezone(tz)
    
        store_uptime = 0
        store_downtime = 0
        
        for day in range(0, 7):
            store_open_time = db.session.query(menu_hours).filter(
                menu_hours.store_id == store_id, menu_hours.day == day).first()
                
            tot_time = (store_open_time.start_time_local - store_open_time.end_time_local).total_seconds() / 3600
            
            naive1 = datetime.datetime.strptime(str(store_open_time.start_time_local), "%H:%M:%S")
            naive2 = datetime.datetime.strptime(str(store_open_time.end_time_local), "%H:%M:%S")
            
            local_cur_time = time_zone.localize(naive1, is_dst=None).astimezone(pytz.utc)
            local_one_week_before_time = time_zone.localize(naive2, is_dst=None).astimezone(pytz.utc)

            store_stats = db.session.query(store_status).filter(
                store_status.store_id == store_id,
                store_status.timestamp_utc.between(local_cur_time, local_one_week_before_time),
                store_status.status == 'active'
                )
            
            uptime_day = store_stats.count()
            downtime_day = tot_time - uptime_day

            if(day == 0):
                uptime_last_hour = db.session.query(store_status).filter(
                    store_status.store_id == store_id,
                    store_status.timestamp_utc.between(local_cur_time, local_cur_time - datetime.timedelta(hours=1)),
                    store_status.status == 'active'
                    ).count()
                
                downtime_last_hour = 1 - uptime_last_hour

            
                uptime_prev_day = db.session.query(store_status).filter(
                    store_status.store_id == store_id,
                    store_status.timestamp_utc.between(local_cur_time, local_cur_time - datetime.timedelta(days=1)),
                    store_status.status == 'active'
                    ).count()
                
                downtime_prev_day = tot_time - uptime_prev_day

            store_uptime += uptime_day
            store_downtime += downtime_day
        
        genreport = report(
            report_id = report_id,
            store_id = store_id,
            uptime_last_hour = uptime_last_hour, 
            uptime_last_day = uptime_prev_day, 
            uptime_last_week = store_uptime, 
            downtime_last_hour = downtime_last_hour, 
            downtime_last_day = downtime_prev_day, 
            downtime_last_week = store_downtime,
        )
        
        db.session.add(genreport)
        db.session.commit()
        

    return report_id

