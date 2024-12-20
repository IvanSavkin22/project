from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from store.servicer.views import repair_center

urlpatterns = [
    path('', main, name='main'),
    path('category/<int:category_id>/', category, name='category'),
    path('product/<int:product_id>/', product, name='product'),
    path('categories/', all_categories, name='all_categories'),
    path('subcategory/<int:subcategory_id>/', subcategory, name='subcategory'),
    path('repair/', repair_center, name='repair_center'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
