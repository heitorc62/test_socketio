from app import app
from extensions import socketio

if __name__ == '__main__':
    print("RUNNING!!!!")
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True, allow_unsafe_werkzeug=True)