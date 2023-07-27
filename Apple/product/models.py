from django.db import models





class Category(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=200,blank=False,null=False)
    category_image=models.ImageField(upload_to='Category_images')
    created=models.DateTimeField(auto_now_add=True)
    offer=models.BooleanField(default=False)
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']


class Products(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=250,blank=False,null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image1=models.ImageField(upload_to='product_image1')
    product_image2=models.ImageField(upload_to='product_image2',null=True,blank=True)
    product_image3=models.ImageField(upload_to='product_image3',null=True,blank=True)
    product_image4=models.ImageField(upload_to='product_image4',null=True,blank=True)
    product_image5=models.ImageField(upload_to='product_image5',null=True,blank=True)
    varient=models.CharField(max_length=150,blank=True,null=True)
    original_price=models.FloatField()
    offer_price=models.FloatField()
    description=models.TextField(max_length=500)
    small_description = models.TextField(max_length=250)
    offer=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.name,self.varient)
    
    class Meta:
        ordering = ['-created']
