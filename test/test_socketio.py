import unittest
from app import create_app
from extensions import socketio
import eventlet


class SocketIOTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.flask_test_client = self.app.test_client()
 

    def tearDown(self):
        pass

    def test_receivement(self):
        # Connect with a valid token
        socketio_test_client = socketio.test_client(self.app, 
                                            flask_test_client=self.flask_test_client)
        
        i = 0
        while (i < 10):
            eventlet.sleep(3)
            r = socketio_test_client.get_received()
            print(f"{i}th response: {r}")
            i += 1
            
            
        