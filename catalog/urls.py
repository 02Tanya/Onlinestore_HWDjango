from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, index

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contact, name="contact"),
    path('', index)]
