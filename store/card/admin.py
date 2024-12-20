from django.contrib import admin
from .models import Payment, Product

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'amount', 'certificate_number', 'created_at')  # Поля для отображения в списке
    search_fields = ('full_name', 'phone_number')  # Поля, по которым можно выполнять поиск
    list_filter = ('created_at',)  # Фильтрация по дате создания

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'full_name', 'phone_number', 'certificate_number', 'amount', 'delivery_address', 'created_at')  # Поля для отображения в списке
    search_fields = ('product_name', 'full_name', 'certificate_number') # Поиск по имени и номеру заказа
    list_filter = ('created_at',)  # Фильтрация по дате создания
