from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def productlist(request):
  productlist = Product.objects.all()
  categorylist = Category.objects.annotate(total_products=Count('product'))
  template = 'Product/product_list.html'
  paginator = Paginator(productlist, 2) 
  page_number = request.GET.get('page')
  productlist = paginator.get_page(page_number) 
  context = {'product_list' : productlist, 'category_list' : categorylist}
  
  return render(request, template, context)
  


def productdetail(request, product_slug):
  productdetail = Product.objects.get(slug=product_slug)
  productimages = ProductImages.objects.filter(product=productdetail)
  template = 'Product/product_detail.html'
  context = {'product_detail': productdetail, 'product_images': productimages}

  return render(request, template, context)