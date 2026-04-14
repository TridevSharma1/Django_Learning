from django.contrib import admin
from django.urls import path
from .views import * ## Importing all views from the current app's views.py file

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categorie', category_products, name='category_products'), # URL pattern for the category_products view
]
