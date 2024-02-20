import eventlet
eventlet.monkey_patch()

from flask import Flask
from extensions import socketio
from socketio_helper import start_redis_listener




def create_app():
    app = Flask(__name__)
    

    from socketio_events import socketio_bp as socketio_blueprint
    app.register_blueprint(socketio_blueprint)
    socketio.init_app(app, logger=True, engineio_logger=True)



    return app


app = create_app()


start_redis_listener()

if __name__ == '__main__':
    print("RUNNING!!!!")
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True, allow_unsafe_werkzeug=True)