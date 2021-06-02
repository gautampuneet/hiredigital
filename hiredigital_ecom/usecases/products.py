# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import Counter, OrderedDict

from django.shortcuts import get_object_or_404

from hiredigital_ecom.models.category import Categories
from hiredigital_ecom.usecases.following import *


def create_product(request):
    """
        Create Product
        params:-
            request - Request Object
        return- Created Product Data
    """
    request_data = json.loads(request.body)
    name = request_data.get("name", "")
    stock = request_data.get("stock", "")
    unit_price = request_data.get("unit_price", "")
    sale_price = request_data.get("sale_price", "")
    user_profile = request_data.get("user_profile", "")
    category = request_data.get("category", "")
    image = request_data.get("image")
    if not name or not user_profile or not category:
        return {"message": "Some Mandatory Fields are missing"}, 400
    if not validate_stock(stock):
        return {"message": "Stock Should be an boolean field"}, 400
    if not validate_user_profile(user_profile):
        return {"message": "User Does Not Exist"}, 400
    if not validate_price(unit_price) or not validate_price(sale_price):
        return {"message": "Prices Should be a number"}, 400
    product_payload = dict()
    category_data = None
    if category:
        category_data, _ = Categories.objects.get_or_create(name__iexact=category, defaults={"user_profile_id": user_profile,
                                                                                             "name": category})
    product_payload["name"] = name
    product_payload["stock"] = stock
    product_payload["unit_price"] = unit_price
    product_payload["sale_price"] = sale_price
    product_payload["user_profile_id"] = user_profile
    product_payload["image"] = image
    product_payload["category_id"] = category_data.id
    products_data = Products.objects.filter(name__iexact=name)
    if products_data.exists():
        return {"message": "Product with this name already exits"}, 400

    product_data = Products.objects.create(**product_payload)
    return product_data, 201


def get_products(request, product_id=None):
    """
        Get All Active Product(We can also sort them based on any key)
        Products Based on User id
        Get Product based on product id
        params:-
            request:- Request Object
        return- Products Object/Objects
    """
    if not product_id:
        user_id = request.GET.get("user_id")
        if user_id:
            products_list = Products.objects.filter(user_profile_id=user_id, is_active=True)
        else:
            products_list = Products.objects.filter(is_active=True)
        order_by = request.GET.get("order_by")
        if order_by:
            products_list = products_list.order_by(order_by)
        return products_list, 200
    else:
        user_profile_id = request.GET.get("user_profile_id")
        if not user_profile_id:
            return {"error": "User Id should be provided"}, 400
        try:
            product_data = get_object_or_404(Products, pk=product_id)
        except Exception:
            return {"error": "Product id {} does not exist".format(product_id)}, 404
        add_product_in_viewed(user_profile_id, product_id)
        return product_data, 200


def update_product(request, product_id):
    """
        Update Product
        params:-
            request:- Request Object
            product_id:- Product id which needed to be updated
        response:- Updated Product Data
    """
    objects = Products.objects.filter(pk=product_id)
    if not objects.exists():
        return {"error": "Product Does not Exist"}, 400
    product_data = objects.first()
    request_data = json.loads(request.body)
    name = request_data.get("name", "")
    stock = request_data.get("stock", "")
    unit_price = request_data.get("unit_price", "")
    sale_price = request_data.get("sale_price", "")
    category = request_data.get("category", "")
    image = request_data.get("image", "")
    if name != product_data.name:
        product = Products.objects.filter(name__iexact=name)
        if product.exists():
            return {"message": "Product With this name already exist"}, 400

    category_data = None
    if category:
        category_data, _ = Categories.objects.get_or_create(name__iexact=category,
                                                            defaults={"user_profile_id": product_data.user_profile.id,
                                                                      "name": category})
    if not validate_stock(stock):
        return {"Stock Should be an boolean field"}, 400
    if unit_price and not validate_price(unit_price):
        return {"Prices Should be a number"}, 400
    if sale_price and not validate_price(sale_price):
        return {"Prices Should be a number"}, 400

    product_data.name = name if name else product_data.name
    product_data.stock = stock if stock != product_data.stock else product_data.stock
    product_data.sale_price = sale_price if sale_price else product_data.sale_price
    product_data.unit_price = unit_price if unit_price else product_data.unit_price
    product_data.category_id = category_data.id if category else product_data.category.id
    product_data.image = image if image else product_data.image
    product_data.save()

    return product_data, 204


def get_recommend_products(request):
    """
        Get Recommended Products
        request:- Request Object
        response:- Products Objects
    """
    user_id = request.GET.get("user_id")
    if not user_id:
        return {"error": "User Id should be provided"}

    following1 = Following.objects.filter(user_profile_id=user_id)
    following1_list = list(following1.values_list("following__id", flat=True))

    if not following1_list:
        return [], 200
    following2 = Following.objects.filter(user_profile_id__in=following1_list, is_active=True
                                          ).exclude(following__id=None)
    following2_list = list(following2.values_list("following__id", flat=True))

    connected_friends = set(following2_list + following1_list)
    if int(user_id) in connected_friends:
        connected_friends.remove(int(user_id))

    products_viewed_obj = ProductsViewed.objects.filter(user_profile_id__in=connected_friends, is_active=True
                                                        ).exclude(products_viewed__id=None)
    products_viewed = list(products_viewed_obj.values_list('products_viewed__id', flat=True))

    if not products_viewed:
        return [], 200
    recommend_product_ids = OrderedDict(Counter(products_viewed).most_common(15)).keys()
    recommended_products = Products.objects.filter(pk__in=recommend_product_ids, is_active=True)
    return recommended_products, 200


