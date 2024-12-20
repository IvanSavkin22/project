from django.shortcuts import get_object_or_404
from store.basket.models import Basket
from .models import Product, Category, Subcategory
from django.shortcuts import render
from django.core.paginator import Paginator


def main(request):
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})


def subcategory(request, subcategory_id):
    active_subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    active_category = active_subcategory.category

    # Извлечение фильтров из запроса
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort')

    # Получаем продукты подкатегории
    products = active_subcategory.subcategory_product.all()

    # Обработка фильтров по цене
    if min_price:
        min_price = float(min_price)
        products = products.filter(price__gte=min_price)

    if max_price:
        max_price = float(max_price)
        products = products.filter(price__lte=max_price)

    # Обработка сортировки
    if sort == 'alphabetical':
        products = products.order_by('title')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    # Пагинация
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Получение всех подкатегорий для отображения
    subcategories = active_subcategory.category.subcategories.all()

    # Проверка на AJAX запрос
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'category/detail.html', {
            'products': page_obj,
        })

    return render(request, 'category/detail.html', {
        'active_category': active_category,
        'active_subcategory': active_subcategory,
        'products': page_obj,
        'subcategories': subcategories,

    })


def category(request, category_id):
    active_category = get_object_or_404(Category, id=category_id)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort')

    products = active_category.category_product.all()

    if min_price:
        min_price = float(min_price)
        products = products.filter(price__gte=min_price)

    if max_price:
        max_price = float(max_price)
        products = products.filter(price__lte=max_price)

    if sort == 'alphabetical':
        products = products.order_by('title')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)


    # Проверка на AJAX запрос
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'category/detail.html', {
            'products': page_obj,
        })

    return render(request, 'category/detail.html', {
        'active_category': active_category,
        'products': page_obj,
        'subcategories': active_category.subcategories.all(),
    })

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/all_categories.html', {'categories': categories})


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket = request.basket
    return render(request, 'product/detail.html', {'product': product, 'basket': basket})

