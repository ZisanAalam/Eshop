
from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Register your models here.



@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','description','category_id')

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','password')
    readonly_fields = ['password']



