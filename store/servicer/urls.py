from django.urls import path
from .views import servicer_name, upgrade_center, repair_center, personalization, services_list, part
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', servicer_name, name='servicer_name'),
    path('services/', services_list, name='services_list'),
    path('repair/', repair_center, name='repair_center'),
    path('upgrade/', upgrade_center, name='upgrade_center'),
    path('personalization/', personalization, name='personalization'),
    path('upgrade_center/', part, name='upgrade_center'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
