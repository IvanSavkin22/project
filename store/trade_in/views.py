from django.shortcuts import render, redirect
from .models import Trade, TradeInRequest

def trade_in(request):
    trades = Trade.objects.all()
    # Получаем все пары из CATEGORY_CHOICES
    unique_categories = Trade.CATEGORY_CHOICES

    context = {
        'trades': trades,
        'unique_categories': unique_categories,
    }
    return render(request, 'trade_in/trade_in.html', context)


def trade_in_submit(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        total_price = request.POST.get('total_price')

        # Проверка, что все данные присутствуют
        if not all([contact_name, contact_email, contact_phone, total_price]):
            return redirect('trade_in')

        # Получаем выбранные товары
        selected_items = []
        for category in Trade.CATEGORY_CHOICES:
            selected_part = request.POST.get(f"{category[0]}_part")
            if selected_part:
                trade_item = Trade.objects.get(id=selected_part)
                selected_items.append(trade_item.name)  # Добавляем название товара в список

        # Преобразуем список в строку
        selected_items_str = ', '.join(selected_items)

        trade_in_request = TradeInRequest(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            total_price=total_price,
            selected_items=selected_items_str  # Сохраняем названия выбранных товаров
        )
        trade_in_request.save()  # Сохраняем объект в базе данных

        return redirect('success_page')
    return redirect('trade_in')


def success_page(request):
    trade_in_request = TradeInRequest.objects.last()
    return render(request, 'trade_in/success_page.html', {'trade_in_request': trade_in_request})
