from flask import Flask

def create_app(configuration='Development'):
    from app.config import config_by_name 
    from app.routes import register_routes
    app = Flask(__name__)
    app.config.from_object(config_by_name[ configuration or 'Development'])
    
    register_routes(app)
    app.run()
    