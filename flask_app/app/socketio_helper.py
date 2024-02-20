from app.extensions import socketio
import redis, eventlet, json

def start_redis_listener():
    # Run the Redis listener in a background thread
    eventlet.spawn(listen_for_redis_messages_from_mqtt_service)

def process_device_update(message_data):
    message = message_data.get('message')
    print(f"UPDATE:: {message}")
    emit_controller_state(message)
    eventlet.sleep(5)


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


def emit_controller_state(data):
    print(f"## Emitting data: {data}")
    socketio.emit('controller_state', data, namespace="/")