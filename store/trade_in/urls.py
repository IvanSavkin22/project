from django.urls import path
from .views import trade_in, trade_in_submit, success_page


urlpatterns = [
    path('', trade_in, name='trade_in'),
    path('submit/', trade_in_submit, name='trade_in_submit'),
    path('success/', success_page, name='success_page'),
]
