from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, one_good, goods_list

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("product/<int:pk>/", one_good, name="one_good"),
    path("catalog/", goods_list, name="goods_list")
]
