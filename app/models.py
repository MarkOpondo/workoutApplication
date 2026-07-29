from app import db

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)