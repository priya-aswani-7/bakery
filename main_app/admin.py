from django.contrib import admin
from .models import Cake, Customer, Order, OrderItem

admin.site.register(Cake)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)