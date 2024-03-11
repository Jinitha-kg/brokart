from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def ProductListView(request):
    return render(request,'products.html')

def ProductDetailView(request):
    return render(request, 'products_detal.html')

