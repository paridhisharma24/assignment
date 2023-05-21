from connect import db
from datetime import datetime

class bq_results(db.Model):
    store_id = db.Column(db.Integer, primary_key=True)
    timezone_str = db.Column(db.String(30))
    