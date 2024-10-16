# Generated by Django 5.1 on 2024-10-04 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание категории",
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите цену", verbose_name="Цена за покупку"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания записи",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату изменения",
                        null=True,
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название категории",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Название категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "ordering": ["name", "category", "price", "created_at", "updated_at"],
            },
        ),
    ]
