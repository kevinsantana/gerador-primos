import os

BROKER = os.environ.get("BROKER", "amqp://rabbitmq:rabbitmq@rabbit:5672/")
