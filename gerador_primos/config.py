import os

BROKER = os.environ.get("BROKER", "amqp://rabbitmq:rabbitmq@172.17.0.2:5672")
