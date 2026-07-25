from django.shortcuts import render

def home(request):
    return render(request, "Dashboard/dashboard.html")
def product_view(request):
    return render(request, "products/product.html" )
# Create your views here.
