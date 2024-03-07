from django.db import models
from django.contrib.auth.models import User

# Model for customer
class CustomerModel(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE, 'Live'), (DELETE, 'Delete'))
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone=models.CharField(max_length=10)  
    creates_at=models.DateTimeField(auto_now_add=True)
    updates_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name