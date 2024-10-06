from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, one_good, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("product/<int:pk>/", one_good, name="one_good"),
    path("catalog/", ProductListView.as_view(), name="goods_list")
]
