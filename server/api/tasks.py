"""This module contains API methods for working with 'tasks'"""

from flask import Blueprint, jsonify
from models import Tasks
from app import db

tasks_module = Blueprint('tasks_module', __name__)


@tasks_module.route('/api/tasks/', methods=['GET'])
def get_tasks():
    """Return tasks"""
        
    tasks = Tasks.query.all()
    return jsonify(tasks=[t.serialize for t in tasks])

