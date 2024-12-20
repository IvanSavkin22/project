from django.db import models

from django.contrib.auth.models import User
from store.product.models import Product
from store.servicer.models import Part


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    log = models.TextField()

    def get_products(self):
        return self.profile_product.all()

class ProfileProduct(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
