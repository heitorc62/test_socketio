import eventlet
eventlet.monkey_patch()

from app.extensions import socketio
from app.socketio_helper import start_redis_listener
from app import create_app


app = create_app()

start_redis_listener()

if __name__ == '__main__':
    print("RUNNING!!!!")
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True, allow_unsafe_werkzeug=True)