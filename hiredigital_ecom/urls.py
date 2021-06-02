# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import path

from hiredigital_ecom.views.product import products_listview, products_view, recommend_products
from hiredigital_ecom.views.following import UpdateFollowing, get_following_by_user
from hiredigital_ecom.views.user_profile import login, get_users

urlpatterns = [
    path('products/', products_listview, name="products_list"),
    path('products/<int:product_id>/', products_view, name="products_view"),
    path('following/<int:following_id>/', UpdateFollowing, name="update_following"),
    path("following", get_following_by_user, name="get_following"),
    path('profiles/', login, name="login"),
    path('profiles/list/', get_users, name="users_list"),
    path('products/recommend/', recommend_products, name="recommend_products")
]