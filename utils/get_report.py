from model.report import report
from connect import db
from flask import jsonify

def get_report(report_id):

    reports = db.session.query(report).filter(report.report_id == report_id).all()

    repo = {}
    for res in reports:
        rept = []
        dict = {}
        dict['store_id'] = res.store_id
        dict['uptime_last_hour'] = res.uptime_last_hour
        dict['uptime_last_day'] = res.uptime_last_day
        dict['uptime_last_week'] = res.uptime_last_week
        dict['downtime_last_hour'] = res.downtime_last_hour
        dict['downtime_last_day'] = res.downtime_last_day
        dict['downtime_last_week'] = res.downtime_last_week

        rept.append(dict)
        repo[res.report_id] = dict
        
    return repo


