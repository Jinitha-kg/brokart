from django.shortcuts import render

# Create your views here.
def ShowAccountView(request):
    return render(request, 'account.html')