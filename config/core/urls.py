from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home),
    path('product/',views.product_view),
]