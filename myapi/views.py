from rest_framework import viewsets

from .models import Myapi
from .serializers import MyapiSerializer

class MyapiViewSet(viewsets.ModelViewSet):
    serializer_class = MyapiSerializer

    def get_queryset(self):
        return Myapi.get()
