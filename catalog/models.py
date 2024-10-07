from django.db import models
from django.db.models import TextField


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
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


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
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Название категории",
        help_text="Введите название категории",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания записи",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения",
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите название заголовка",
    )
    slug = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="slug",
    )
    body = TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое"
    )
    image = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите фото",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания записи",
        help_text="Введите дату создания",
    )
    is_published = models.BooleanField(
        default=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения",
    )
    view_count = models.IntegerField(
        default=0,
        blank=True,
        verbose_name="Количество просмотров",
        help_text="Количество просмотров",
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "created_at", "is_published", "view_count"]

    def __str__(self):
        return self.title


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="versions",
        null=True,
        blank=True,
        verbose_name="Версия для продукта",
    )
    version_number = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name="Номер версии",
        help_text="Укажите номер версии",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Признак текущей версии",
        help_text="Признак, является ли данная версия текущей",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "is_active", "name"]

    def __str__(self):
        return f'{self.name}'
