import altair as alt
import pandas as pd
import os
import json
from kafka import KafkaConsumer, KafkaProducer
from time import sleep

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'localhost:9092')
GRAPHS_TOPIC = os.environ.get('GRAPHS_TOPIC', 'viz.sentences.graphs')

gameSessionId = "aze"
playerId = "noua"
name="unasada"
title="Analyse des sentiments asdasdasda"
message = {'headers': {'gameSessionId': gameSessionId, 'playerId': playerId, 'beginsAt': '2020-07-16T13:27:48.328Z', 'endsAt': '2020-07-16T13:27:54.508Z'}, 'data': {'name': name, 'title': title, 'type': name, 'data': '{\n "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json",\n "config": {\n "view": {\n "continuousHeight": 300,\n "continuousWidth": 700\n }\n },\n "data": {\n "name": "data-c0767d4f624d61cd6aa8e99f695f560b"\n },\n "datasets": {\n "data-c0767d4f624d61cd6aa8e99f695f560b": [\n {\n "date": "2020-07-16T13:26:45.608Z",\n "talking": 1\n },\n {\n "date": "2020-07-16T13:26:46.358Z",\n "talking": 0\n },\n {\n "date": "2020-07-16T13:27:23.318Z",\n "talking": 1\n },\n {\n "date": "2020-07-16T13:27:24.878Z",\n "talking": 0\n },\n {\n "date": "2020-07-16T13:27:38.148Z",\n "talking": 1\n },\n {\n "date": "2020-07-16T13:27:39.918Z",\n "talking": 0\n },\n {\n "date": "2020-07-16T13:27:48.328Z",\n "talking": 1\n },\n {\n "date": "2020-07-16T13:27:54.508Z",\n "talking": 0\n }\n ]\n },\n "encoding": {\n "x": {\n "field": "date",\n "type": "temporal"\n },\n "y": {\n "field": "talking",\n "type": "quantitative"\n }\n },\n "mark": {\n "interpolate": "step-after",\n "type": "area"\n }\n}'}}


if __name__ == "__main__":

    print("Connecting to kafka...")
    # Create the producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    print(message)  # DEBUG
    producer.send(GRAPHS_TOPIC, value=message)
    sleep(1)