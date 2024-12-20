from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.core.management.base import BaseCommand
from .models import Basket, Line
from store.product.models import Product
from store.servicer.models import Part


def basket_add(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        basket = request.basket

        existing_line = basket.basket_lines.filter(product=product).first()
        if existing_line:
            existing_line.quantity += 1
            existing_line.price += product.price
            existing_line.save()
            message = "Товар уже в корзине."
        else:
            Line.objects.create(product=product, basket=basket, price=product.price)
            message = "Товар добавлен в корзину!"

        return JsonResponse({
            'total_items': basket.basket_lines.count(),
            'message': message
        })


def upgrade_center(request, part_id):
    if request.method == 'POST':
        part = get_object_or_404(Part, id=part_id)
        basket = request.basket

        existing_line = basket.basket_lines.filter(part=part).first()
        if existing_line:
            existing_line.quantity += 1
            existing_line.price += part.price
            existing_line.save()
            message = "Товар уже в корзине."
        else:
            # Проверяем, что у части есть цена
            if part.price is not None:  # или если в вашем случае может быть < 0
                Line.objects.create(part=part, basket=basket, price=part.price)
                message = "Товар добавлен в корзину!"
            else:
                message = "Ошибка: у товара нет установленной цены."

        return JsonResponse({
            'total_items': basket.basket_lines.count(),
            'message': message,
        })


def basket_remove(request, line_id):
    if request.method == 'POST':
        basket = request.basket
        basket.basket_lines.filter(id=line_id).delete()
        return redirect('basket_detail')


def basket_detail(request):
    basket = request.basket
    return render(request, 'basket/detail.html', {'basket': basket})


class Command(BaseCommand):
    help = 'Clean up empty baskets'

    def handle(self, *args, **options):
        empty_baskets = Basket.objects.filter(basket_lines__isnull=True)
        count, deleted = empty_baskets.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted} empty baskets'))
