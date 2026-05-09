from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api')

from app.tasks import routes