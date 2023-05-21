from connect import db

class report(db.Model):
    report_id = db.Column(db.String(10), primary_key=True)
    store_id = db.Column(db.Integer)
    uptime_last_hour = db.Column(db.Integer) 
    uptime_last_day = db.Column(db.Integer) 
    uptime_last_week = db.Column(db.Integer) 
    downtime_last_hour = db.Column(db.Integer) 
    downtime_last_day = db.Column(db.Integer) 
    downtime_last_week = db.Column(db.Integer)
