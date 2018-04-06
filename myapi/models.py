from django.db import models
from pymemcache.client.base import Client
import json


# Create your models here.
class Myapi(models.Model):
    print('myapi model!')
    mykey = models.CharField(max_length=100)
    myval = models.CharField(max_length=100)

    def json_serializer(key, value):
         if type(value) == str:
             return value, 1
         return json.dumps(value), 2

    def json_deserializer(key, value, flags):
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value)
        raise Exception("Unknown serialization format")


    cache = Client(('localhost', 11211),
    serializer=json_serializer,
    deserializer=json_deserializer)

    blorp = ['foo', {'bar': ('baz', None, 1.0, 2)}]
    cache.set('foo', blorp)

    def save(self, *args, **kwargs):
        print('saving!')

    def get(self, *args, **kwargs):
        return cache.get('foo')
