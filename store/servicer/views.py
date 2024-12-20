from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Part, Appointment, PersonalizationRequest
from .forms import AppointmentForm, PersonalizationForm


def servicer_name(request):
    return render(request, 'servicer/servicer_name.html')


def part(request):
    part_list = Part.objects.all()

    # Получаем значения фильтров
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_order = request.GET.get('sort_order')

    # Фильтрация по цене
    if min_price:
        part_list = part_list.filter(price__gte=min_price)
    if max_price:
        part_list = part_list.filter(price__lte=max_price)

    # Сортировка
    if sort_order == 'name_asc':
        part_list = part_list.order_by('name')  # Сортировка по имени А-Я
    elif sort_order == 'name_desc':
        part_list = part_list.order_by('-name')  # Сортировка по имени Я-А

    # Пагинация
    paginator = Paginator(part_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Проверяем, является ли запрос AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Проверка на AJAX-запрос
        return render(request, 'servicer/upgrade_center.html', {
            'parts_pc': page_obj,
        })

    return render(request, 'servicer/upgrade_center.html', {
        'parts_pc': page_obj,
        'page_obj': page_obj,
    })


def upgrade_center(request):
    parts_pc = Part.objects.filter(category='pc')
    return render(request, 'servicer/upgrade_center.html', {
        'parts_pc': parts_pc,
    })


def repair_center(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'servicer/repair_center.html', {'message': 'Заявка отправлена, ожидайте звонка.'})
    else:
        form = AppointmentForm()
    return render(request, 'servicer/repair_center.html', {'form': form})


def personalization(request):
    if request.method == 'POST':
        form = PersonalizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personalization')  # Перенаправление на ту же страницу
    else:
        form = PersonalizationForm()
    return render(request, 'servicer/personalization.html', {'form': form})


def services_list(request):
    services = [
        {'name': 'Апгрейд центр', 'url': 'upgrade_center'},
        {'name': 'Ремонт и диагностика', 'url': 'repair_center'},
        {'name': 'Трейд ин', 'url': 'trade_in'},
        {'name': 'Персонализация', 'url': 'personalization'},
    ]
    return render(request, 'servicer/services_list.html', {'services': services})
