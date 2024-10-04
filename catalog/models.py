from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите фото продукта",
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену"
    )
    created_at = models.DateField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Дата создания записи",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name.plural = "Продукты"
        ordering = ["category", "price", "created_at", "updated_at"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name.plural = "Категории"

    def __str__(self):
        return self.name
