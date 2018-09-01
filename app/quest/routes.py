from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.quest.forms import InitialQuestionForm, NewRecordForm
from app.models import User, Post, Records
from app.translate import translate
from app.quest import bp

@bp.route('/initial_questions', methods=['GET', 'POST'])
def initial_questions():
    form = InitialQuestionForm()
    return render_template('quest/initial_questions.html',
                                title=('TLFB - Questionnaire'), form=form)

@bp.route('/new_record', methods=['GET', 'POST'])
def new_record():
    form = NewRecordForm()
    return render_template('quest/new_record.html',
                                title=('TLFB - New Record'), form=form)
