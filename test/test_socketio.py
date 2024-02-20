import unittest, json, time
from app import create_app
from extensions import socketio
import eventlet


class SocketIOTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.flask_test_client = self.app.test_client()
 

    def tearDown(self):
        pass

    def test_request_device_state(self):
        # Connect with a valid token
        socketio_test_client = socketio.test_client(self.app, 
                                            flask_test_client=self.flask_test_client)
        
        socketio_test_client.emit('request_device_state')
        eventlet.sleep(1)
        r = socketio_test_client.get_received()
        print(f"response = {r}")
        self.assertTrue(len(r) == 1)
        self.assertTrue(r[0]['name'] == 'controller_state')
        self.assertTrue(len(r[0]['args']) == 1)