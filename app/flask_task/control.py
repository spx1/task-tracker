from flask import Flask, Blueprint, render_template, abort, Response

from app import TEMPLATE_DIR
from app.model import Task
from app.interface import TaskInterface
from app.service import TaskService
from app.schema import TaskSchema
from app.flask_task import BASE_ROUTE

api = Blueprint('task-tracker',__name__,
    url_prefix=f'/{BASE_ROUTE}',
    template_folder=TEMPLATE_DIR)

@api.route('/', defaults={"page": "index"})
@api.route('/<page>')
def show(page):
    try:
        #return f'task tracker ({page})'
        return render_template('health_check.html',msg=page)
    except:
        abort(404)

@api.route('/app/get_all')
def get_all():
    try:
        print('Entering get_all')
        schema = TaskSchema(many=True)
        return Response(response= schema.dumps(TaskService.get_all()),status="200",mimetype="application/json")
    except:
        abort(404)