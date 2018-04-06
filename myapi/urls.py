from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapi import views


router = DefaultRouter()
router.register('myapi', views.MyapiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
