from django.db import models
from datetime import  datetime
# Create your models here.

class Blog(models.Model):
    image = models.CharField(max_length=100000,default="",blank=True)
    header = models.CharField(max_length=100)
    text = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now,blank=True)

class Urban_user(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    box = models.JSONField(default=list)
    email = models.EmailField()
    password = models.CharField()
    user_name = models.CharField(default="")



class Latest_produce(models.Model):
    img = models.CharField()
    category = models.CharField()
    product_name = models.CharField()
    product_description = models.CharField()
    price = models.IntegerField()
    per = models.CharField()
    discount = models.BooleanField(default=False)
    discount_percent = models.IntegerField(default=0)
    def get_discount_price(self):
        discount_price = (self.discount/100) * self.price 
        discount_price *= 10
        discount_price = (self.price - discount_price) 
        return discount_price
        
