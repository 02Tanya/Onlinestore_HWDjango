from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.models import Product
from catalog.views import home, contact, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="one_good"),
    path("catalog/", ProductListView.as_view(), name="goods_list")
]
