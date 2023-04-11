from flask_wtf import FlaskForm

# from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
    TextAreaField,
    BooleanField,
    validators,
    DateField,
    TimeField,
)
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from stackunderflow_app.models import Users


class AddQuestionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=140)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(max=5000)])