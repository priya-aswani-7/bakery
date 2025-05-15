from django.db import models
from django.utils import timezone

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.flavor})"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default = timezone.now)
    
    @property
    def total_price(self):
        order_items = self.orderitem_set.all()
        total = sum(item.quantity * item.cake.price for item in order_items)
        return total

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'cake')

    def __str__(self):
        return f"Order {self.order.id} item: {self.cake.name} x {self.quantity}"
