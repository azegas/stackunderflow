from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(20), default="default.jpg")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.String(5000))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship(
        "Users", backref="questions"
    )  # allows to access the name of the author instead of id
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )  # onupdate method allows to specify an SQL expression that will
    # be executed when the row is updated


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship("Users")
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    question = db.relationship("Question", backref=db.backref("answers", lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
