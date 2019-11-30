from flask import Flask,Blueprint

def register_routes(app):
    from app.flask_task.control import api
    app.register_blueprint(api)