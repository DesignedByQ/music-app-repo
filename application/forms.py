from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired

class SongForm(FlaskForm):
    ntitle = StringField('Song Title', validators=[DataRequired()])
    nartist = StringField('Artist', validators=[DataRequired()])
    nfeature = StringField('Feature')
    ncategory = StringField('Category', validators=[DataRequired()])
    nreldate = DateField('Release Date', validators=[DataRequired()])
    nlength = StringField('Length', validators=[DataRequired()])
    submit = SubmitField('Add Song')
    