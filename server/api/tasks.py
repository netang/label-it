"""This module contains API methods for working with 'tasks'"""

from flask import Blueprint, jsonify
from models import Tasks
from app import db

tasks_module = Blueprint('tasks_module', __name__)


@tasks_module.route('/api/tasks/', methods=['GET'])
def get_tasks():
    """Return tasks"""
        
    # tasks = Tasks.query.all()
    tasks = [{"id": 1, "name": "Разметка медицинских текстов", 
    "description": "Ребят, тут есть просьба немного разметить топики, в каждом файле всего лишь по 50 примеров (!)\n\nОценки:\n4 - есть явная тема, \"фоновые\"* слова присутствуют единично (1-3)\n3 - есть явная тема при существенном наличии \"фоновых\" слов\n2 - есть явная тема, но присутствуют вкрапления несвязанных с ней слов\n1 - топик представляет собой смесь 2-3 тем\n0 - не понятно, о чем топик\n\n* \"фоновые\" - слова явно не принадлежащие какой-либо теме, общие\n\nЖелательно сделать сегодня, это где-то 30-60 минут :)", 
    "progress": "430/1033", "initiator": "Датасайнтист №7"}]
    return jsonify(tasks=tasks)

