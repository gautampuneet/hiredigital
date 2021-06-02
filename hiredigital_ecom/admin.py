from django.contrib import admin
# Register your models here.

from hiredigital_ecom.models.following import Following
from hiredigital_ecom.models.category import Categories
from hiredigital_ecom.models.product import Products
from hiredigital_ecom.models.user_profile import UserProfile
from hiredigital_ecom.models.products_viewed import ProductsViewed

admin.site.register(Following)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(UserProfile)
admin.site.register(ProductsViewed)
