def register_routes(app):
    from app.flask_task import register_routes as FlaskTask
    FlaskTask(app)
