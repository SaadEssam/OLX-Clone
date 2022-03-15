from django.shortcuts import render
from .models import Product, ProductImages
from django.core.paginator import Paginator

# Create your views here.

def productlist(request):
  productlist = Product.objects.all()
  template = 'Product/product_list.html'
  paginator = Paginator(productlist, 5) 
  page_number = request.GET.get('page')
  productlist = paginator.get_page(page_number) 
  context = {'product_list' : productlist}
  
  return render(request, template, context)
  


def productdetail(request, product_slug):
  productdetail = Product.objects.get(slug=product_slug)
  productimages = ProductImages.objects.filter(product=productdetail)
  template = 'Product/product_detail.html'
  context = {'product_detail': productdetail, 'product_images': productimages}

  return render(request, template, context)