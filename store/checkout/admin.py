from django.contrib import admin

from .models import *
from store.profiles.models import ProfileProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def add_product(self, request, queryset):
        for order in queryset:
            for line in order.basket.basket_lines.all():
                product = line.product

                ProfileProduct.objects.create(product=product, profile=order.user.profile)
                order.status = Order.Status.COMPLETED
                order.save()