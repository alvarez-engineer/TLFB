from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, \
                    IntegerField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import Records

class InitialQuestionForm(FlaskForm):
    alcohol = SelectField(_l('Have you had a drink of alcohol since (DoLV)'),
                            choices=[('yes', 'Yes'),('no','No')])
    marijuana = SelectField(_l('Have you used marijuana since (DoLV)'),
                            choices=[('yes', 'Yes'),('no','No')])
    tobacco = SelectField(_l('Have you used tobacco/nicotine since (DoLV)'),
                            choices=[('yes', 'Yes'),('no','No')])
    other = SelectField(_l('Have you used any other substance (other than \
                            above) that were not prescribed to you since \
                            (DoLV)'), choices=[('yes', 'Yes'),('no','No')])

class NewRecordForm(FlaskForm):
    subject = StringField(_l('Study ID: '), validators=[DataRequired()])
    start = DateField(_l('Start date:'), format='%m-%d-%Y',
                        validators=[DataRequired()])
    end = DateField(_l('End date:'), format='%m-%d-%Y',
                        validators=[DataRequired()])
    days = IntegerField(_l('How many days back'), validators=[DataRequired()])
    submit = SubmitField(_l('Start'))
