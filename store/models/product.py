from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_categoryId(category_id):
        return Product.objects.filter(category = category_id)