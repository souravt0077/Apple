from django.db import models
from user.models import User
from product.models import Products

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.product.name,self.user.username)
    
    class Meta:
        ordering = ['-added_on']