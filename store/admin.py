from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock']
    search_fields = ("name__startswith",)


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'email']
    search_fields = ("phone__startswith",)


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'product', 'price', 'quantity', 'total', 'address', 'phone', 'date', 'status']
    search_fields = ("phone__startswith",)


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)

admin.site.site_header = 'KD Fresh Dashboard'
admin.site.site_title = 'Dashboard'
admin.site.index_title = 'Dashboard'
