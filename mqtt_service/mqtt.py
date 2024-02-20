import redis, threading, json

redis_client_sender = redis.Redis(host='redis', port=6379, db=2)

def process_publish_mqtt_command():
    print(f"Processing MQTT publish command")
    redis_client_sender.publish('device_update', json.dumps({"message": "Device OK"}))

def listen_for_redis_from_main_service():
    redis_client = redis.Redis(host='redis', port=6379, db=2)
    pubsub = redis_client.pubsub()
    pubsub.subscribe(['mqtt_subscribe', 'mqtt_publish'])

    for message in pubsub.listen():
        if message['type'] == 'message':
            channel = message['channel'].decode()
            if channel == 'mqtt_publish':
                data = json.loads(message['data'])
                print(f"Received MQTT publish command: {data}")
                process_publish_mqtt_command()


def main():
    print("MQTT Service starting...")
    thread = threading.Thread(target=listen_for_redis_from_main_service)
    thread.start()

if __name__ == "__main__":
    main()
