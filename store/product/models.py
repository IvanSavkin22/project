from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url


class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='category_product')
    subcategory = models.ForeignKey(Subcategory, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='subcategory_product')
    graphics_card = models.CharField(max_length=255, default='N/A')
    processor = models.CharField(max_length=255, default='N/A')
    motherboard = models.CharField(max_length=255, default='N/A')
    battery = models.CharField(max_length=255, default='N/A')
    ram = models.CharField(max_length=255, default='N/A')
    ssd = models.CharField(max_length=255, default='N/A')
    is_laptop = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url


class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    product = models.ForeignKey(Product, related_name='product_lecture', on_delete=models.CASCADE)
    stage = models.ImageField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['stage', ]


class Material(models.Model):
    class MaterialType(models.TextChoices):
        TEXT = 'text', 'Text'
        IMAGE = 'image', 'Image'
        VIDEO = 'video', 'Video'
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media', blank=True, null=True)
    material_type = models.CharField(choices=MaterialType, default=MaterialType.TEXT, max_length=20)
    lecture = models.ForeignKey(Lecture, related_name='lectuere_material', on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['stage', ]




