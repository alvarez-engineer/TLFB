from datetime import datetime, date
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, session
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.quest.forms import InitialQuestionForm, NewRecordForm
from app.models import User, Post, Records
from app.translate import translate
from app.quest import bp
import simplejson as json

@bp.route('/initial_questions', methods=['GET', 'POST'])
@login_required
def initial_questions():
    subject = session['subject']
    start = session['start']
    end = session['end']
    days = session['days']
    form = InitialQuestionForm()
    if form.validate_on_submit():
        record = Records(alcohol=form.alcohol.data, marijuana=form.marijuana.data,
                                    tobacco=form.tobacco.data, other=form.other.data )
        # db.session.add(record)
        # db.session.commit()
        flash(_('Time line follow back time!'))
        # record this as one database and then pop the sessions
        return redirect(url_for('calendar.calendar'))
    return render_template('quest/initial_questions.html',
                                title=('TLFB - Questionnaire'), form=form, subject=subject, start=start,
                                end=end, days=days)

@bp.route('/new_record', methods=['GET', 'POST'])
@login_required
def new_record():
    today = date.today().strftime('%m-%d-%Y')
    form = NewRecordForm()
    if form.validate_on_submit():
        session['subject'] = form.subject.data
        session['start'] = form.start.data.strftime('%m-%d-%Y')
        session['end'] = form.end.data
        session['days'] = form.days.data
        return redirect(url_for('quest.initial_questions'))
    return render_template('quest/new_record.html',
                                            title=('TLFB - New Record'), form=form, today=today)
