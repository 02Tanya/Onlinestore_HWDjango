from django import forms
from django.forms import BooleanField
from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def clean_name(self):
        """Валидация содержимого наименования продукта"""
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        cleaned_data = self.cleaned_data["name"]

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("Такое название для продукта недопустимо")

        return cleaned_data

    def clean_description(self):
        """Валидация описания продукта"""
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        cleaned_data = self.cleaned_data["description"]

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("Такое описание для продукта недопустимо")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ("product", "version_number", "name")
