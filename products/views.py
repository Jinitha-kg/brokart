from django.shortcuts import render
from . models import ProductModel
from django.core.paginator import Paginator
# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def ProductListView(request):
    page=1
    if request.GET:
        page=request.GET.get('page', 1)
    product_list=ProductModel.objects.all()

    produc_paginator=Paginator(product_list,3)
    product_list=produc_paginator.get_page(page)

    context={'products':product_list}
    return render (request,'products.html', context)

def ProductDetailView(request):
    return render(request, 'products_details.html')

