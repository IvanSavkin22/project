from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортируем для проверки аутентификации
import random
from .models import Product, Payment
from store.basket.models import Basket


class SuccessView(View):
    def get(self, request, certificate_number):
        return render(request, 'card/success.html', {
            'success': True,
            'certificate_number': certificate_number,
        })


class CertificateView(View):
    def get(self, request):
        current_year = datetime.now().year
        years = list(range(current_year, current_year + 11))
        return render(request, 'card/certificate.html', {'years': years})

    def post(self, request):
        selected_amount = request.POST.get('amount')
        if selected_amount:
            return redirect('gift_certificate', amount=selected_amount)
        return redirect('certificate')


class ProductCertificateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, amount=None, type=None):
        template_name = 'card/gift_certificate.html' if type == 'certificate' else 'card/gift_cards.html'
        return render(request, template_name, {
            'years': list(range(datetime.now().year, datetime.now().year + 11)),
            'amount': amount,
        })

    def post(self, request, type=None, amount=None):
        return self.process_payment(request, type, amount)

    def process_payment(self, request, type, amount=None):
        full_name = request.POST.get('full_name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        delivery_address = request.POST.get('delivery_address', '').strip()
        amount = request.POST.get('amount', '').strip()
        errors = []

        if not all([full_name, phone_number, amount]):
            errors.append("Все поля должны быть заполнены.")

        if errors:
            template_name = 'card/gift_certificate.html' if type == 'certificate' else 'card/gift_cards.html'
            return render(request, template_name, {
                'years': list(range(datetime.now().year, datetime.now().year + 11)),
                'errors': errors,
                'full_name': full_name,
                'phone_number': phone_number,
                'delivery_address': delivery_address,
                'amount': amount,
            })

        certificate_number = random.randint(100000, 999999)

        try:
            basket = Basket.objects.get(owner=request.user)
        except Basket.DoesNotExist:
            errors.append("Корзина не найдена.")
            return render(request, 'card/gift_cards.html', {'errors': errors})

        # Проверяем наличие строк в корзине
        if not basket.basket_lines.exists():
            errors.append("Корзина пуста.")
            return render(request, 'card/gift_cards.html', {'errors': errors})

        # Получаем имена всех продуктов в корзине
        product_names = [line.product.title for line in basket.basket_lines.all() if line.product]
        product_name = ', '.join(product_names)

        if delivery_address:
            Product.objects.create(
                product_name=product_name,
                full_name=full_name,
                phone_number=phone_number,
                certificate_number=certificate_number,
                amount=amount,
                delivery_address=delivery_address,
            )

            basket.clear()

        else:
            Payment.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                certificate_number=certificate_number,
                amount=amount,
            )

        # Перенаправление на страницу успеха
        return redirect('success', certificate_number=certificate_number)
