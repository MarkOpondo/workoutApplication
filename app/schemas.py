from marshmallow import fields, validate, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Exercise, Workout, WorkoutExercises
from app import db

class ExerciseSchema(SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    category = fields.String(validate=validate.Length(max=50))
    equipment_needed = fields.Bool(load_default=False)
    class Meta:
        model = Exercise
        fields = ("id","name","category","equipment_needed")
        sqla_session = db.session
        load_instance = True
        ordered = True


class WorkoutExercisesSchema(SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(load_default=0, validate=validate.Range(min=0))
    sets = fields.Int(load_default=0, validate=validate.Range(min=0))
    duration = fields.Int(load_default=0, validate=validate.Range(min=0))

    exercise = fields.Nested(ExerciseSchema, only=["name", "category"])
    class Meta:
        model = WorkoutExercises
        fields = ("id","workout_id","exercise_id","reps", "sets", "duration", "exercise")
        load_instance = True
        sqla_session = db.session
        ordered = True


class WorkoutSchema(SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(format="iso", dump_only=True)
    duration_minutes = fields.Int(load_default = 0, validate=validate.Range(min=0))
    notes = fields.Str(validate=validate.Length(max=200))

    exercises = fields.List(fields.Nested(WorkoutExercisesSchema, exclude=["workout_id"]), dump_only=True)
    class Meta:
        model = Workout
        fields = ("id", "date", "duration_minutes", "notes", "exercises")
        sqla_session = db.session
        load_instance = True
        ordered = True


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExercisesSchema()
workout_exercises_schema = WorkoutExercisesSchema(many=True)