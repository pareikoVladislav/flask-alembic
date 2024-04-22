from flask import Flask
from flask_migrate import Migrate

from extensions import db
from config import Config

from first_app.models.dog_case import DogCaseModel
from first_app.models.evidence import Evidence
from first_app.models.victims import Victims


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


if __name__ == '__main__':
    app = create_app()
    app.run()
