from flask import Flask

def create_app():
    """App factory"""
    app = Flask(__name__)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .sonos import sonos as sonos_blueprint
    app.register_blueprint(sonos_blueprint, url_prefix='/sonos')

    return app
