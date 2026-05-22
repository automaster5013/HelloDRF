#example/urls.py
from django.urls import path, include
from example.views import HelloAPI

urlpatterns = [
    path("hello/", HelloAPI),
]
