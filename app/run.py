import eventlet
eventlet.monkey_patch()

from app import create_app
from extensions import socketio

app = create_app()


def listen():
    while(True):
        socketio.emit('test', dict(foo="bar"), namespace="/")
        eventlet.sleep(2)
        
    
                
eventlet.spawn(listen)


if __name__ == '__main__':
    print("RUNNING!!!!")
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True, allow_unsafe_werkzeug=True)