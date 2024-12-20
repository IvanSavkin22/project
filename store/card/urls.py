from django.urls import path
from .views import ProductCertificateView, CertificateView, SuccessView

urlpatterns = [
    path('certificate/', CertificateView.as_view(), name='certificate'),
    path('cards/certificate/<str:amount>/', ProductCertificateView.as_view(), {'type': 'certificate'}, name='gift_certificate'),
    path('cards/product/<str:amount>/', ProductCertificateView.as_view(), {'type': 'product'}, name='gift_cards'),
    path('success/<int:certificate_number>/', SuccessView.as_view(), name='success'),
]