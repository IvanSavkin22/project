from .models import Basket


class BasketMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        basket_id = request.session.get('basket_id')
        if basket_id:
            try:
                basket = Basket.objects.get(id=basket_id)
            except Basket.DoesNotExist:
                # Если корзина не найдена, создаем новую
                basket = Basket.objects.create()
        else:
            basket = Basket.objects.create()

        if request.user.is_authenticated:
            if not basket.owner:
                # Закрываем все открытые корзины пользователя, если это необходимо
                request.user.baskets.filter(status=Basket.Status.OPEN).update(status=Basket.Status.CLOSED)
                basket.owner = request.user
                basket.save()

        # Обновляем ID корзины в сессии
        request.session['basket_id'] = basket.id  # Изменено на basket.id
        request.basket = basket
        response = self.get_response(request)
        return response
