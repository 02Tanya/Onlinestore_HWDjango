from gc import get_objects
from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from pytils.templatetags.pytils_translit import slugify

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
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogDetailView(DetailView):
    model = Blog

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.view_count += 1
    #     self.object.save()
    #     return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image')
    # success_url = reverse_lazy('list')


class BlogDeleteView(DetailView):
    model = Blog
    success_url = reverse_lazy('list')