from django.db import models


# Create your models here.
class Customer(models.Model):
    First_name = models.CharField(max_length=250)
    Last_name = models.CharField(max_length=250)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.First_name
class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    img = models.ImageField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.product_name
