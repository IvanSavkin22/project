from store.product.models import *
from store.servicer.models import *
from django.shortcuts import render


def product_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def context(request):
    categories = Category.objects.all()
    parts = Part.objects.all()  # Это может остаться, если вам нужно

    # Можно просто передать список фиксированных услуг
    services = [
        {'name': 'Апгрейд центр', 'url': 'upgrade_center'},
        {'name': 'Ремонт и диагностика', 'url': 'repair_center'},
        {'name': 'Трейд ин', 'url': 'trade_in'},
        {'name': 'Персонализация', 'url': 'personalization'},
    ]

    return {
        'categories': categories,
        'parts': parts,
        'services': services
    }