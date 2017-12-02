from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('username', validators=[DataRequired()])


class PasswordForm(FlaskForm):
    password = StringField('password', validators=[DataRequired()])


class MessageForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])