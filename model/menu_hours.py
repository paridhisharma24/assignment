from connect import db
from datetime import datetime

class menu_hours(db.Model):
    store_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    start_time_local = db.Column(db.DateTime, default = datetime.utcnow)
    end_time_local = db.Column(db.DateTime, default = datetime.utcnow)
