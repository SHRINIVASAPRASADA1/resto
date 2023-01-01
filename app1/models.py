from django.db import models

# Create your models here.

class BestMenu(models.Model):
    Title=models.TextField(blank=False,null=False)
    Description=models.TextField(blank=False,null=False)
    amount=models.IntegerField(blank=False,null=False)
    img=models.ImageField(blank=False,null=False,upload_to="menu/")
    Date=models.DateTimeField(blank=False,null=False,auto_now=True)
    subTitle=models.TextField(blank=True)
    Ratting=models.IntegerField(blank=False,null=True)

    def __str__(self):
        return str(self.Title)


class CarouselSlider(models.Model):
    Title=models.TextField(blank=False,null=False)
    Description=models.TextField(blank=False,null=False)
    amount=models.IntegerField(blank=False,null=False)
    img=models.ImageField(blank=False,null=False,upload_to="menu/")
    Date=models.DateTimeField(blank=False,null=False,auto_now=True)
    subTitle=models.TextField(blank=True)
    Ratting=models.IntegerField(blank=False,null=True)

    def __str__(self):
        return str(self.Title)



class AddToCart(models.Model):
    food_id=models.TextField(blank=False,null=False)
    User=models.TextField(blank=False,null=False,default="unknown")
    title=models.TextField(blank=False,null=False)
    img=models.TextField(blank=False,null=False)
    amount=models.IntegerField(blank=True,null=True)
    date=models.DateTimeField(blank=False,null=False,auto_now=True)


    def __str__(self) -> str:
        return str(self.date)

class BuyNow(models.Model):
    product_id=models.TextField(blank=False,null=False)
    users=models.TextField(blank=False,null=False)
    phonenumber=models.TextField(blank=False,null=False)
    city=models.TextField(blank=False,null=False)
    state=models.TextField(blank=False,null=False)
    pincode=models.TextField(blank=False,null=False)
    address=models.TextField(blank=False,null=False)
    amount=models.TextField(blank=False,null=False)
    quant=models.TextField(blank=False,default=1)

    def __str__(self) -> str:
        return str(self.users)