from datetime import date
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, \
                    IntegerField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
# from app.models import Records

class CalendarForm(FlaskForm):
    alcohol_yes = BooleanField(_l('Alcohol: '))
    alcohol_times = IntegerField(_l('Number of drinks: '), validators=[DataRequired()])
    alcohol_type = StringField(_l('Type of Alcohol'), validators=[DataRequired()])

    mj_yes = BooleanField(_l('Marijuana '))
    mj_times = IntegerField(_l('Times per day: '), validators=[DataRequired()])
    mj_gram = IntegerField(_l('How many grams: '), validators=[DataRequired()])

    tobacco_yes = BooleanField(_l('Tabacco'))
    tobacco_type =  RadioField(_l('Holder for Electronic or normal cig', choices = [('M','Male'),('F','Female')]))
    tobacco_times = IntegerField(_l('Times per day: '), validators=[DataRequired()])
