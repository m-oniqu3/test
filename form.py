from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired,  FileAllowed
from wtforms.validators import DataRequired , Email, validators, ValidationError


class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()], id="fname")
    lastname = StringField('Lastname', validators=[DataRequired()], id="lname")
    gender = SelectField('Gender',  choices=[('S','Select Gender'), ('Female', 'Female'), ('Male', 'Male')], id="gender")
    email = StringField('Email',[validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "e.g. jdoe@example.com "}, id="email")
    location = StringField ('Location', validators=[DataRequired()], render_kw={"placeholder": "e.g. Kingston,Jamaica "}, id="location")
    biograpy = TextAreaField ('Biography', validators=[DataRequired()], id="bio")
    picture = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'PNG'], 'Images only!')],id="profilepicture")

    firstname = StringField('Firstname', validators=[DataRequired()], id="fname")
    lastname = StringField('Lastname', validators=[DataRequired()], id="lname")
    gender = SelectField('Gender',  choices=[('S','Select Gender'), ('Female', 'Female'), ('Male', 'Male')], id="gender")
    email = StringField('Email',[validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "e.g. jdoe@example.com "}, id="email")
    location = StringField ('Location', validators=[DataRequired()], render_kw={"placeholder": "e.g. Kingston,Jamaica "}, id="location")
    biograpy = TextAreaField ('Biography', validators=[DataRequired()], id="bio")
    picture = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'PNG'], 'Images only!')],id="profilepicture")
