from datetime import datetime, timezone
from app import db


class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50))
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_sessions = db.relationship('WorkoutExercises', back_populates='exercise', cascade="all, delete-orphan")


class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    duration_minutes = db.Column(db.Integer, default=0)
    notes = db.Column(db.String(200))

    exercises = db.relationship('WorkoutExercises', back_populates='workout', cascade="all, delete-orphan")

class WorkoutExercises(db.Model):
    __tablename__ = 'workoutexercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    reps = db.Column(db.Integer, default=0)
    sets = db.Column(db.Integer, default=0)
    duration = db.Column(db.Integer, default=0)

    workout = db.relationship('Workout', back_populates='exercise')
    exercise = db.relationship('Exercise', backpopulates='workout_sessions')