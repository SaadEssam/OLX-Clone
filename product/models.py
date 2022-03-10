from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
  
  CONDITION_TYPE = (
    ("New", "New") ,
    ("Used", "Used")
  )
  
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField(max_length=500)
  condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
  price = models.DecimalField(max_digits=10, decimal_places=5)
  created_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.name
  