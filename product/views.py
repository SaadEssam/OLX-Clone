from django.shortcuts import render
from .models import Product, ProductImages
# Create your views here.

def productlist(request):
  productlist = Product.objects.all()
  template = 'Product/product_list.html'
  context = {'product_list' : productlist}
  
  return render(request, template, context)
  


def productdetail(request, product_slug):
  productdetail = Product.objects.get(slug=product_slug)
  productimages = ProductImages.objects.filter(product=productdetail)
  template = 'Product/product_detail.html'
  context = {'product_detail': productdetail, 'product_images': productimages}

  return render(request, template, context)