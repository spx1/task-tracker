from flask import Flask, Blueprint, render_template, abort
from app import TEMPLATE_DIR

api = Blueprint('task-tracker',__name__,
    url_prefix='/task-tracker',
    template_folder=TEMPLATE_DIR)

@api.route('/', defaults={"page": "index"})
@api.route('/<page>')
def show(page):
    try:
        #return f'task tracker ({page})'
        return render_template('health_check.html',msg=page)
    except:
        abort(404)