from contextlib import nullcontext
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
  
  CONDITION_TYPE = (
    ("New", "New") ,
    ("Used", "Used")
  )
  
  city_choice = (
  ('Alexandria', 'Alexandria'),
  ('Aswan', 'Aswan'),
  ('Asyut', 'Asyut'),
  ('Beheira', 'Beheira'),
  ('Beni Suef', 'Beni Suef'),
  ('Cairo', 'Cairo'),
  ('Dakahlia', 'Dakahlia'),
  ('Damietta', 'Damietta'),
  ('Fayoum', 'Fayoum'),
  ('Gharbia', 'Gharbia'),
  ('Giaz', 'Giza'),
  ('Ismailia', 'Ismailia'),
  ('Kafr al-Sheikh', 'Kafr al-Sheikh'),
  ('Luxor', 'Luxor'),
  ('Matruh', 'Matruh'),
  ('Minya', 'Minya'),
  ('Monufia', 'Monufia'),
  ('New Valley', 'New Valley'),
  ('Port Said', 'Port Said'),
  ('Qalyubia', 'Qalyubia'),
  ('Qena', 'Qena'),
  ('Red Sea', 'Red Sea'),
  ('Sharqia', 'Sharqia'),
  ('Sohag', 'Sohag'),
  ('South Sinai', 'South Sinai'),
  ('Suez', 'Suez'),
  )
  
  
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  description = RichTextField()
  condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
  category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
  brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
  city = models.CharField(choices=city_choice, max_length=100)
  price = models.IntegerField()
  image = models.ImageField(upload_to='main_product/', blank=True, null=True)
  created_date = models.DateTimeField(default=timezone.now)
  slug = models.SlugField(blank=True, null=True)
  
  def save(self, *args, **kwargs):
    if not self.slug and self.name :
      self.slug = slugify(self.name)
    super(Product, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.name
  
  
class ProductImages(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='products/', blank=True, null=True)
  
  
  class Meta:
    verbose_name = 'Product Image'
    verbose_name_plural = 'Product Images'
    
    
  def __str__(self):
    return self.product.name
  
  
class Category(models.Model):
  category_name = models.CharField(max_length=50)
  image = models.ImageField(upload_to='category/', blank=True, null=True)
  slug = models.SlugField(blank=True, null=True)
  
  def save(self, *args, **kwargs):
    if not self.slug and self.category_name : 
      self.slug = slugify(self.category_name)
    super(Category, self).save(*args, **kwargs)
  
  
  class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'
    
  def __str__(self):
    return self.category_name
  
  

class Brand(models.Model):
  brand_name = models.CharField(max_length=50)
  
  class Meta:
    verbose_name = 'brand'
    verbose_name_plural = 'brands'
    
  def __str__(self):
    return self.brand_name