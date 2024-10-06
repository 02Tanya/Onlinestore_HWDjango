from gc import get_objects
from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product, Category, Blog

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

# def goods_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product_list.html', context)

# def one_good(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context)


def goods(request):
    return render(request, "catalog/product_list.html")


def home(request):
    return render(request, "catalog/home.html")


def contact(request):
    return render(request, "catalog/contact.html")


def index(request):
    if request.method == "post":
        name = request.post.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "contact.html")

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('home')

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog

class BlogDeleteView(DetailView):
    model = Blog