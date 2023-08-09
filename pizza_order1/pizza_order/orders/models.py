from django.db import models
from ingredients.models import Ingredients
from django.utils import timezone
from uuid import uuid4

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable = False)
    dough = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='crusts')
    sauce = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='sauces')
    meat_products = models.ManyToManyField(Ingredients, related_name='meat_products')
    cheese = models.ManyToManyField(Ingredients, related_name='cheeses')
    spicery = models.ManyToManyField(Ingredients, related_name='spices')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_cooking_time = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Order {self.id}"
    
    def remaining_time(self):
        current_time = timezone.now()
        time_elapsed = (current_time - self.created_at).total_seconds() / 60
        remaining_time = max(self.max_cooking_time - time_elapsed, 0)
        return round(remaining_time)
    