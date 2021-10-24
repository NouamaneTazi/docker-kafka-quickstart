"""Produce fake sentences into a Kafka topic."""

import os
from time import sleep
import json
from kafka import KafkaProducer
import datetime

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'localhost:9092')
EVENT_TOPIC = os.environ.get('EVENT_TOPIC', 'event.events')
GAME_ENDING_EVENT = os.environ.get('GAME_ENDING_EVENT')

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    event = {
        "headers": {
            "gameSessionId": "game_1594804711150",
            "playerId": "player_1594810456158",
        },
        "data": GAME_ENDING_EVENT,
    }
    producer.send(EVENT_TOPIC, value=event)
    print(event)  # DEBUG
    sleep(1)  # important or else message dont get sent
