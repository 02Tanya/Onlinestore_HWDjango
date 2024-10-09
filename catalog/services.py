from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    '''При возможности получает список категорий из кэш. В противном случае, обращается к БД'''
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'categories_list'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set("categories_list", categories)
    return categories