from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, goods

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("", goods, name="goods")
]
