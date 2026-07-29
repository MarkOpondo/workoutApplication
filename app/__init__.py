from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

from config import config_by_name

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    migrate = Migrate(app, db)
    db.init_app(app)
    @app.get("/")
    def index():
        return jsonify(message="My workout app")
    
    return app