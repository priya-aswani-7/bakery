from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
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
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Add M:M relationship with Cake through OrderItem
    cakes = models.ManyToManyField(Cake, through='OrderItem')
    
    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
        
class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order #{self.order.id} - {self.cake.name} x {self.quantity}"
        
    class Meta:
        # Prevent duplicate cake entries in an order
        unique_together = ('order', 'cake')