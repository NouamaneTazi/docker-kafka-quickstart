"""Example Kafka consumer."""

import json
import os

from kafka import KafkaConsumer, KafkaProducer
import datetime


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TOPIC = os.environ.get('SENTENCES_TOPIC')
PLAYER1_TOPIC = os.environ.get('PLAYER1_TOPIC')
PLAYER2_TOPIC = os.environ.get('PLAYER2_TOPIC')

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')


def player1_talking(sentences: dict) -> bool:
    """Find the player that's talking."""
    return sentences['player'] == 'player1'


print("### KAFKA_BROKER_URL", KAFKA_BROKER_URL)
if __name__ == '__main__':
    print("Connecting...")
    consumer = KafkaConsumer(
        TOPIC,
        group_id='group1',
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    print(f"Connected to {TOPIC} topic!")
    for message in consumer:
        sentences: dict = message.value
        # Send to queue
        topic = PLAYER1_TOPIC if player1_talking(sentences) else PLAYER2_TOPIC
        producer.send(topic, value=sentences)
        print(datetime.datetime.now().time(), sentences)  # DEBUG
