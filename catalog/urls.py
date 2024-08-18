from django.urls import path, include
from catalog.apps import NewappConfig

app_name = NewappConfig.name

urlpatterns = [
    path('',)
]