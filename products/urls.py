from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('product_list', views.ProductListView, name='list_product'),
]