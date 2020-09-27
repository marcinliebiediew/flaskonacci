from datetime import datetime

from src.extensions import db


class Logs(db.Model):
    timestamp = db.Column(db.DateTime,
                          primary_key=True,
                          default=lambda: datetime.now())
    path_and_method = db.Column(db.String(50), nullable=False)
    request_data = db.Column(db.Integer, nullable=False)
    response_data = db.Column(db.String(20), nullable=False)
