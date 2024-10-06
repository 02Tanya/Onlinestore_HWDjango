from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, goods, goods_list

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("", goods_list)
]
