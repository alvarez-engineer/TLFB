from flask import Blueprint

bp = Blueprint('quest', __name__)

from app.quest import routes
