import requests
import json
import time
from kafka import *

from requests import get


def getTemperature():
    _json_data = 'NO Data'
    try:
        res = requests.get(
            'https://samples.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b6907d289e10d714a6e88b30761fae22')
        json_data = json.dumps(res.json())
        print(type(json_data))
        print(json_data)

    except Exception as E:
        print(str(E))
    finally:
        return json_data


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(producer=None):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    while (1):
        data = getTemperature()
        kafka_producer = connect_kafka_producer()
        publish_message(kafka_producer, 'raw_recipes', 'raw', data)
        time.sleep(2)

    # /home/spark/odmc/weather.json
