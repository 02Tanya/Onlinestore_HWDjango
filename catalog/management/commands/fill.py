import json
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(
            "/Users/tatyanasharapova/PycharmProjects/SkyPro/Homeworks/HW20.1/Onlinestore_HWDjango/catalog_data.json",
            "r",
            encoding="utf-8",
        ) as file:
            categories = json.load(file)
            return categories

    @staticmethod
    def json_read_products():
        with open(
            "/Users/tatyanasharapova/PycharmProjects/SkyPro/Homeworks/HW20.1/Onlinestore_HWDjango/catalog_data.json",
            "r",
            encoding="utf-8",
        ) as file:
            products = json.load(file)
            return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            if category["model"] == "catalog.category":
                category_for_create.append(
                    Category(
                        name=category["fields"]["name"],
                        description=category["fields"]["description"],
                        pk=category["pk"],
                    )
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            if product["model"] == "catalog.product":
                product_for_create.append(
                    Product(
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        price=product["fields"]["price"],
                        image=product["fields"]["image"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                    )
                )

        Product.objects.bulk_create(product_for_create)
