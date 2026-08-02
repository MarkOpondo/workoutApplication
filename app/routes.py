from flask import Blueprint, jsonify, request
from app import db
from app.models import Exercise, Workout, WorkoutExercises
from app.schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema,
    workout_exercises_schema
)

bp = Blueprint('api', __name__)

@bp.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200

@bp.get("/exercises/<int:id>")
def get_exercise(id):
    exercise = db.session.get(Exercise, id)

    if exercise is None:
        return jsonify(error="not_found", message="Exercise not found"), 404
    return jsonify(exercise_schema.dump(exercise)), 200

@bp.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200

@bp.get("/workouts/<int:id>")
def get_workout(id):
    workout = db.session.get(Workout, id)
    if workout is None:
        return jsonify(error="not_found", message="Workout not found"), 404
    return jsonify(workout_schema.dump(workout)), 200