
from extensions import socketio
from flask import Blueprint, request

socketio_bp = Blueprint('socketio', __name__)

@socketio.on('connect')
def handle_connect(auth):
    print(f"Socket.IO client connected: {request.sid}")