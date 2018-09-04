from datetime import datetime, date
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
# from app.calendar.forms import InitialQuestionForm, NewRecordForm
from app.models import User, Post, Records
from app.translate import translate
from app.calendar import bp

@bp.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar/calendar.html',
                                title=('TLFB - Calendar'))
