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

@bp.post("/exercises")
def create_exercise():
    exercise = exercise_schema.load(request.get_json() or {})
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(exercise)), 201

@bp.delete("/exercises/<int:id>")
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)
    if exercise is None:
        return jsonify(error="Exercise not found")

    db.session.delete(exercise)
    db.session.commit()
    return jsonify(messsage="Exercise deleted successfully"), 200

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

@bp.post("/workouts")
def add_workout():
    workout = workout_schema.load(request.get_json() or {})
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout_schema.dump(workout)), 201

@bp.delete("/workouts/<int:id>")
def delete_workout(id):
    workout = db.session.get(Workout, id)
    if workout is None:
        return jsonify(error="Workout not found")

    db.session.delete(workout)
    db.session.commit()
    return jsonify(messsage="Workout deleted successfully"), 200


@bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_workout_exercise(workout_id, exercise_id):
    if not Workout.query.get(workout_id):
        return jsonify(error="Workout not found"), 404
    
    if not Exercise.query.get(exercise_id):
        return jsonify(error="Exercise not found"), 404
    
    data = request.get_json() or {}

    new_we = WorkoutExercises(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get("reps", 0),
        sets=data.get("sets", 0),
        duration_seconds=data.get("duration_seconds", 0)
    )

    db.session.add(new_we)
    db.session.commit()

    return jsonify(workout_exercise_schema.dump(new_we)), 201