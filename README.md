# workoutApplication
A comprehensive, production-ready RESTful API built with Flask, Flask-SQLAlchemy, and Flask-Marshmallow to track exercises, log custom workouts, and manage nested metric associations across sessions.

## Project Description
This application acts as a performance management tool for gym workouts. It maps a Many-to-Many relationship between **Workouts** and **Exercises** via a highly detailed structural junction table (**WorkoutExercises**). This setup enables tracking metrics like reps, sets, and durations for each movement per workout session, preventing data loss across tables using safe database cascade deletes.

---

## Installation Instructions

Follow these step-by-step setup sequences inside your system terminal to install and configure your environment variables:

### 1. Rebuild the Virtual Environment
Ensure you are located inside the project root directory and install all required package hooks tracked in the `Pipfile`:
```bash
pipenv install
```

### 2. Activate the Environment Shell
Spawn a clean shell instance locked into your specific project dependencies:
```bash
pipenv shell
```

### 3. Initialize and Run Database Migrations
Create your local migrations tracking repository and apply the structural tables down to your local SQLite storage footprint:
```bash
flask db init
flask db migrate -m "Initial migration with exercise models"
flask db upgrade
```

### 4. Seed the Database
Populate your database tables with dummy data records for testing and verification:
* If your file is in the root directory:
  ```bash
  python seed.py
  ```

---

## Run Instructions

Start the localized development server on your configured network port (**5005**) by running the main entry script directly:

```bash
python run.py
```
Your server will deploy locally at: `http://127.0.0`

---

## API Endpoints Matrix

All endpoints are registered under the structural `/api` path routing namespace.

### Workout Endpoints
* **`GET /api/workouts`**
  * **Description:** Lists all tracked workouts currently in the database.
* **`GET /api/workouts/<id>`**
  * **Description:** Fetches a single workout session details, automatically embedding full relational metrics (`reps`, `sets`, `duration_seconds`) for all exercises.
* **`POST /api/workouts`**
  * **Description:** Creates a brand new workout tracking record.
* **`DELETE /api/workouts/<id>`**
  * **Description:** Permanently drops a workout record, cascading deletion to wipe out linked items in the junction tracking logs.

### Exercise Endpoints
* **`GET /api/exercises`**
  * **Description:** Lists all unique movement exercise profiles available.
* **`GET /api/exercises/<id>`**
  * **Description:** Shows specific details for an exercise along with its dynamic chronological historical performance metrics.
* **`POST /api/exercises`**
  * **Description:** Instantiates a new exercise profile.
* **`DELETE /api/exercises/<id>`**
  * **Description:** Deletes an exercise from the system database catalog, clearing related session configurations.

### Advanced Relational Entry Endpoints
* **`POST /api/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`**
  * **Description:** Appends an exercise profile to an existing workout ledger instance. Expects optional JSON configurations mapping performance rows (`reps`, `sets`, `duration_seconds`).

---

## Project Dependencies Configuration (`Pipfile`)

Your environment dependencies map precisely inside your `Pipfile` configuration layout:

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
werkzeug = "*"
flask = "*"

[dev-packages]

[requires]
python_version = "3.14"
```