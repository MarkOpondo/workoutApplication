from datetime import datetime, timezone
from app import create_app, db
from app.models import Exercise, Workout, WorkoutExercises

app = create_app('development')

with app.app_context():
    db.session.query(Exercise).delete()
    db.session.query(Workout).delete()
    db.session.query(WorkoutExercises).delete()

    exercises = [
        Exercise(name="Push Ups", category="Chest", equipment_needed=False),
        Exercise(name="Dumbbell Bicep Curls", category="Arms", equipment_needed=True)
    ]

    workouts = [
        Workout(date=datetime.now(timezone.utc), duration_minutes=45, notes="Morning upper body routine"),
        Workout(date=datetime.now(timezone.utc), duration_minutes=30, notes="Quick leg workout blast")
    ]

    db.session.add_all(exercises + workouts)
    db.session.flush()

    workout_exercises = [
        # Connects the first workout to the first exercise
        WorkoutExercises(workout_id=workouts[0].id, exercise_id=exercises[0].id, reps=15, sets=4, duration=5),
        # Connects the second workout to the second exercise
        WorkoutExercises(workout_id=workouts[1].id, exercise_id=exercises[1].id, reps=12, sets=3, duration=8)
    ]

    db.session.add_all(workout_exercises)
    db.session.commit()