import argparse
import socketio
import sys

# Create an argument parser to accept the server URL as a command-line argument
parser = argparse.ArgumentParser(description="Socket.io client")
parser.add_argument("server_url", nargs='?', 
                    default="http://localhost:5000", 
                    const="http://localhost:5000", 
                    help="URL of the server to connect to (default: http://localhost:5000)")
args = parser.parse_args()

# Use the URL provided as the server URL
server_url = args.server_url

sio = socketio.Client()

@sio.event
def connect():
    print('(INFO) Connection established')
    # Start the user input loop
    user_input_loop()


@sio.on('controller_state')
def on_message(message):
    print(f'\n\n(FROM SERVER - controller_state)\n{message}\n\n')


@sio.event
def disconnect():
    print('\n\n(INFO) Disconnected from server\n\n')


def user_input_loop():
    while True:
        event_name = input("(INPUT) Enter the event name (request_device_state or 'exit' to disconnect):\n")
        if event_name == "request_device_state":
            sio.emit("request_device_state")
            continue
        if event_name == "exit":
            # Disconnect when the user chooses to exit
            sio.disconnect()
            sys.exit(0)
            
print(server_url)
sio.connect(url=server_url)
sio.wait()


