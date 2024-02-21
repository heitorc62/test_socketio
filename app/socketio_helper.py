from extensions import socketio
import redis, eventlet, json



def process_device_update(message_data):
    message = message_data.get('message')
    print(f"UPDATE:: {message}")
    emit_controller_state(message)
    eventlet.sleep(5)





def emit_controller_state(data):
    print(f"## Emitting data: {data}")
    socketio.emit('controller_state', data, namespace="/")