from django.shortcuts import render, redirect
from store.basket.models import Basket
from .models import Order
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


def preview(request):
    basket = request.basket
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        order = Order.objects.create(user=request.user, basket=basket, total_price=basket.get_total_price())

        basket.status = Basket.Status.CLOSED
        basket.save()
        request.session['order_id'] = order.id

        return redirect('checkout_success')
    return render(request, 'checkout/preview.html', {'basket': basket})


def success(request):
    return render(request, 'checkout/success.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    error_message = None

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('checkout_success')
        else:
            error_message = "Неверный логин или пароль."

    return render(request, 'login.html', {'login_form': form, 'error_message': error_message})
