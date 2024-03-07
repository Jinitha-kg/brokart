from django.db import models
from customers.models import CustomerModel
from products.models import ProductModel


# data models for order
class OrderModel(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE, 'Live'), (DELETE, 'Delete'))

    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED, "ORDER_PROCESSED"),
                   (ORDER_DELIVERED, "ORDER_DELIVERED"),
                   (ORDER_REJECTED, "ORDER_REJECTED")
                   )
    
    order_status=models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner=models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


# model for ordered items
class OrdereditemModel(models.Model):
    product=models.ForeignKey(ProductModel, related_name='added_carts', on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='added_items')

