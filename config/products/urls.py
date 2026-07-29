from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.product_view, name ="product_view"),
    path('add-product/', views.add_product, name = "add_product")
]