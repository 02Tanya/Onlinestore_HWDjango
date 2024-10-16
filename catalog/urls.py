from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.models import Product
from catalog.views import (
    home,
    contact,
    ProductListView,
    ProductDetailView,
    BlogCreateView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, CategoryListView,
    # VersionCreateView,
    # VersionUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="one_good"),
    path("catalog/", ProductListView.as_view(), name="goods_list"),
    path("catalog:create/", ProductCreateView.as_view(), name="create_good"),
    path("catalog:edit/<int:pk>/", ProductUpdateView.as_view(), name="edit_good"),
    path("catalog:delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_good"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("list/", BlogListView.as_view(), name="list"),
    path("view/<int:pk>/", BlogDetailView.as_view(), name="view"),
    path("edit/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    # path("catalog:create/", VersionCreateView.as_view(), name='create_version'),
    # path("catalog:edit/<int:pk>/", VersionUpdateView.as_view(), name='edit_version'),
]
