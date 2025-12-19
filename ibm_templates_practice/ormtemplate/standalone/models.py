# standalone/models.py
from django.db import models


# Test model
class Test(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

# new table
class Order(models.Model):
    order_id = models.CharField(max_length = 50, unique = True)
    order_data = models.DateField(auto_now_add = True)
    is_shipped = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Order {self.order_id}"
