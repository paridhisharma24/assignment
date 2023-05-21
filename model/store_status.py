from connect import db
from datetime import datetime

class store_status(db.Model):
    store_id = db.Column((db.Integer), primary_key=True)
    status = db.Column(db.String(10))
    timestamp_utc = db.Column(db.DateTime, default = datetime.utcnow)
    