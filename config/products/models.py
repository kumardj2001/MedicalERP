from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descripton = models.TextField()
    image = models.ImageField(upload_to="products/")
    catalogue = models.FileField(upload_to= "products/")
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    stock_quantity = models.IntegerField(default = 0)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

# if we dont use related_name the we have to write like this-> category.product_set.all() 