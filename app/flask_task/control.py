from flask import Flask, Blueprint, render_template, abort

api = Blueprint('task-tracker',__name__,
    url_prefix='/task-tracker',
    template_folder="templates")

@api.route('/', defaults={"page": "index"})
@api.route('/<page>')
def show(page):
    try:
        return f'task tracker ({page})'
    except:
        abort(404)