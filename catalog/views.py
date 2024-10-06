from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from catalog.models import Product, Category

def goods_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'goods.html', context)

# def one_good(request):
#     onegood = Product.objects.get(pk=pk)
#     context = {"products": products}
#     return render(request, 'goods.html', context)


def goods(request):
    return render(request, "goods.html")

# def onegood(request):
#     return render(request, "onegood.html")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def index(request):
    if request.method == "post":
        name = request.post.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "contact.html")