import eventlet
eventlet.monkey_patch()

from flask import Flask
from extensions import socketio
import redis, json
from socketio_helper import process_device_update


def create_app():
    app = Flask(__name__)
    

    from socketio_events import socketio_bp as socketio_blueprint
    app.register_blueprint(socketio_blueprint)
    socketio.init_app(app, logger=True, engineio_logger=True)



    return app


app = create_app()

def listen_for_redis_messages_from_mqtt_service():
    redis_client = redis.Redis(host='redis', port=6379, db=2)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('device_update')

    for message in pubsub.listen():
        if message['type'] == 'message':
            # Deserialize the message data
            channel = message['channel'].decode()
            data = json.loads(message['data'])
            if channel == 'device_update':
                process_device_update(data)



eventlet.spawn(listen_for_redis_messages_from_mqtt_service)
