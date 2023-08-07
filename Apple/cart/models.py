from django.db import models
from user.models import User
from product.models import Products

# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.product,self.user)
    
    class Meta:
        ordering=['-added_on']
    