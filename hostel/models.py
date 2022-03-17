from django.db import models
# Create your models here.


class Hostel(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    description = models.CharField(max_length=250,blank=True,null=True)
    price = models.CharField(max_length=50,blank=True,null=True)
    stock = models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='uploads/' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
