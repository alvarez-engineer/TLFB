from datetime import date
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, \
                    IntegerField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import Records

class InitialQuestionForm(FlaskForm):
    alcohol = SelectField(_l('Have you had a drink of alcohol since (DoLV)'),
                            choices=[('no','No'),('yes', 'Yes')])
    marijuana = SelectField(_l('Have you used marijuana since (DoLV)'),
                            choices=[('no','No'),('yes', 'Yes')])
    tobacco = SelectField(_l('Have you used tobacco/nicotine since (DoLV)'),
                            choices=[('no','No'),('yes', 'Yes')])
    other = SelectField(_l('Have you used any other substance (other than \
                            above) that were not prescribed to you since \
                            (DoLV)'), choices=[('no','No'),('yes', 'Yes')])
    submit = SubmitField(_l('Submit'))

class NewRecordForm(FlaskForm):
    subject = StringField(_l('Study ID: '), validators=[DataRequired()])
    start = DateField(_l('Start date:'), format='%m-%d-%Y', default=date.today,
                        validators=[DataRequired()])
    end = DateField(_l('End date: (or date of last visit)'), format='%m-%d-%Y',
                        validators=[DataRequired()])
    days = IntegerField(_l('How many days back'), validators=[DataRequired()])
    submit = SubmitField(_l('Start'))
