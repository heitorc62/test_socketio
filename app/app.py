from flask import Flask
from extensions import socketio


def create_app():
    app = Flask(__name__)
    from socketio_events import socketio_bp as socketio_blueprint
    app.register_blueprint(socketio_blueprint)
    socketio.init_app(app, logger=True, engineio_logger=True)
    return app
