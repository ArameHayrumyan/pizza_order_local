from django.db import models
from django.db import models
# Create your models here.


class Ingridient(models.Model):
     name = models.CharField(max_length=25)