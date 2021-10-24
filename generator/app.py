"""Produce fake sentences into a Kafka topic."""

import os
from time import sleep
import json
from kafka import KafkaProducer
from stream import generate_random_sentence
import datetime 

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'localhost:9092')
TOPIC = os.environ.get('SENTENCES_TOPIC', 'text-stream')
SENTENCES_PER_SECOND = float(os.environ.get('SENTENCES_PER_SECOND', 1))
SLEEP_TIME = 1 / SENTENCES_PER_SECOND


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while True:
        sentences: dict = generate_random_sentence()
        producer.send(TOPIC, value=sentences)
        print(datetime.datetime.now().time(), sentences)  # DEBUG
        sleep(SLEEP_TIME)
