from application import db 
from datetime import datetime

class SoccerMgmt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #type = db.Column(db.String(30), default='player', nullable=False)
    name = db.Column(db.String(30), nullable=False)
    age_group = db.Column(db.String(30), nullable=False)
    position = db.Column(db.String(30), nullable=False)
    fav_club = db.Column(db.String(30), default='Real Madrid', nullable=False)
    day = db.Column(db.String(30))
    #date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    # amount = db.Column(db.Integer, nullable=False)
    
    def __str__(self):
        return str(self.id)
#action="{{ url_for('submit_form') }}