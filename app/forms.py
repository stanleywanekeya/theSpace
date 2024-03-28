from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,\
        TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,\
        Length
from app import db
import sqlalchemy as sa
from app.models import User

class LoginForm(FlaskForm):
    """Class implementation of the login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """Class implementation of the registration form"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Validates if the username is already in the database or not"""
        user = db.session.scalar(
                sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please user a different username')

    def validate_email(self, email):
        """Validates if email is already in the database or not"""
        user = db.session.scalar(
                sa.select(User).where(User.username == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address')

class EditProfileForm(FlaskForm):
    """Provides form to edit the profile"""
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        """Initializes the form"""
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        """validates the username entered"""
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == self.username.data))
            if user is not None:
                raise ValidationError('Please use a different username')

class EmptyForm(FlaskForm):
    """Form for the follow button"""
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    """Form for users to publish posts"""
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    """Form that requests password reset"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    """Form to reset the users password"""
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
