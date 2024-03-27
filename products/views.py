from django.shortcuts import render
from . models import ProductModel
# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def ProductListView(request):
    product_list=ProductModel.objects.all()
    context={'products':product_list}
    return render (request,'products.html', context)

def ProductDetailView(request):
    return render(request, 'products_details.html')

