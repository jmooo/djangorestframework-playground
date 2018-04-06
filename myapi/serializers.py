from rest_framework import serializers

from myapi.models import Myapi


class MyapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myapi
        fields = ('mykey', 'myval')
