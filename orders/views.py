from django.shortcuts import render

# Create your views here.
def ShowCartView(request):
    return render(request, 'cart.html')