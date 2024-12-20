from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import basket_add, basket_detail, basket_remove, upgrade_center
from store.card.views import ProductCertificateView

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:line_id>/', basket_remove, name='basket_remove'),
    path('detail/', basket_detail, name='basket_detail'),
    path('cards/', ProductCertificateView.as_view(), name='gift_cards'),
    path('upgrade_center/<int:part_id>/', upgrade_center, name='upgrade_center'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
