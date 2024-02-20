
from extensions import socketio
from flask import Blueprint, request
import json
import redis, json

redis_mqtt_socketio_client = redis.Redis(host='redis', port=6379, db=2)
    

socketio_bp = Blueprint('socketio', __name__)

@socketio.on('connect')
def handle_connect(auth):
    print(f"Socket.IO client connected: {request.sid}")


@socketio.on('request_device_state')
def handle_request_device_state():
    redis_mqtt_socketio_client.publish('mqtt_publish', 
                                       json.dumps({"message": "Requesting device state"}))