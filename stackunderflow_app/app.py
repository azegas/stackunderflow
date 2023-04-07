import os
from flask import Flask

basedir = os.path.dirname(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "db.sqlite"
    )

    flask_secret_key = os.urandom(32)
    app.config["SECRET_KEY"] = flask_secret_key

    from stackunderflow_app.models import db

    # we are telling SQLAlchemy that this app is going to use this
    # database instance for its database operations
    db.init_app(app)

    # creates an application context for the Flask application, which
    # allows the application to access the necessary resources for
    # database creation
    with app.app_context():
        # creates all the tables defined by the application models
        db.create_all()

    from . import auth

    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route("/")
    def index():
        return "Hello, World, this is index page!"

    return app


app = create_app()