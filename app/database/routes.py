from datetime import datetime, date
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, session
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
# from app.database.forms import InitialQuestionForm, NewRecordForm
from app.models import User, Post, Records
from app.translate import translate
from app.database import bp

@bp.route('/database', methods=['GET', 'POST'])
@login_required
def database():
    record = Records.query.all()
    return render_template('database/user_database.html', record=record,
                                title=('TLFB - Database'))
