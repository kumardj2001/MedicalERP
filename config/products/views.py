from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_view(request):
    product_list = Product.objects.all()
    # product_1 = get_object_or_404(Product, name='ECG')
  
    return render(request, "product_temp/product.html", {'product_list':product_list,
                                                        
    })
def add_product(request):
    Product.objects.create(
        name="ECG Machine",
        price=50000,
        descripton="12 Channel ECG",
        is_active=True
    )

    return render(request, "product_temp/product.html")
def update_product(request):
    product = Product.objects.get_object_or_404(name='ECG Machine')
    product.name = "ECG MACHINE"
    product.save()

    # EVERY TIME WE DO   PRODUCT.SAVE() DJANGO CALLS THE MODEL'S DAVE METHOD
    # AND We CAN CUSTOMIZE THAT METHOD.
    # from django.utils.text import slugify
    # class Product(models.Model):

    #     name = models.CharField(max_length=100)
    #     slug = models.SlugField()

    #     def save(self, *args, **kwargs):
    #         self.slug = slugify(self.name)
    #         super().save(*args, **kwargs)

    # overriding delete.
    # def delete(self, *args, **kwargs):
    #       print("")
    #       super().delete(*args, **kwargs)