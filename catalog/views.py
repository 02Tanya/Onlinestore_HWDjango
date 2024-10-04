from django.shortcuts import render


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
