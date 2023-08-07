from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

class IngredientsTypes(models.Choices):
    Dough = 'Dough'
    Spicery = 'Spicery'
    Sauce = 'Sauce'
    Meat_products = 'Meat_products'
    Cheese = 'Cheese'   


# Create your models here.
class Ingredients(models.Model):

    class Meta:
        db_table = 'ingredient'
        verbose_name = _('Ingredients')
        verbose_name_plural = _('Ingredients')
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=IngredientsTypes.choices)
    time = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)

class IngredientsManager(models.Manager):
    def get_dough(self):
        return self.filter(type=IngredientsTypes.Dough)

    def get_spicery(self):
        return self.filter(type=IngredientsTypes.Spicery)

    def get_sauce(self):
        return self.filter(type=IngredientsTypes.Sauce)

    def get_meat_products(self):
        return self.filter(type=IngredientsTypes.Meat_products)

    def get_cheese(self):
        return self.filter(type=IngredientsTypes.Cheese)

   #Create your models here.
