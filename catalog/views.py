from gc import get_objects
from itertools import product
from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.templatetags.pytils_translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Category, Blog, Version
from catalog.services import get_categories_from_cache


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:goods_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST)
        else:
            context_data["formset"] = ProductFormset()
        return context_data

    def form_valid(self, form):
        new_product = form.save()
        new_product.owner = self.request.user
        new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:goods_list")

    def get_success_url(self, *args, **kwargs):
        return reverse("catalog:one_good", args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if form.is_valid() and formset.is_valid():

            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
        # else:
        #     return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit_is_published") and user.has_perm("catalog.can_edit_description") and user.has_perm("catalog.can_edit_category"):
            return ProductModeratorForm
        raise PermissionDenied



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:goods_list")


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
    fields = ("title", "body", "image")
    success_url = reverse_lazy("catalog:list")

    def form_valid(self, form):
        """Метод для генерирования slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Метод для вывода содержимого по признаку"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Метод для счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save(update_fields=["view_count"])
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "body", "image")

    # success_url = reverse_lazy('list')
    def form_valid(self, form):
        """Метод для генерирования slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:view", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:list")


# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     # fields = ('name', 'description', 'image', 'category', 'price')
#     success_url = reverse_lazy('catalog:catalog')

#     def form_valid(self, form):
#         if form.is_valid():
#             new_version = form.save()
#             new_version.product = Product.objects.get(pk=self.kwargs.get('<int:pk>'))
#             new_version.save()
#         return super().form_valid(form)
#
#
#
# class VersionUpdateView(UpdateView):
#     model = Version
#     form_class = VersionForm
#     # fields = ('name', 'description', 'image', 'category', 'price')
#     success_url = reverse_lazy('catalog:catalog')
