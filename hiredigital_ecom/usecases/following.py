# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from hiredigital_ecom.models.following import Following
from hiredigital_ecom.models.products_viewed import ProductsViewed
from utils.validations import *


def update_following(request, following_id):
    """
        Update Following
        params:
         request - Request Object
         following_id - Following Id which needed to be updated
        return:- Following Object, Status Code
    """
    request_data = json.loads(request.body)
    following = request_data.get("following", [])
    if not validate_following(following):
        return {"error": "Following Should be a list of Existing users"}, 400
    objects = Following.objects.filter(pk=following_id)
    if not objects.exists():
        return {"error": "Following Does not Exist"}, 400

    following_data = objects.first()
    if following:
        following_data.following.clear()
        following_data.following.add(*following)
    return following_data, 204


def add_product_in_viewed(user_profile_id, product_id):
    """
        Add Product in User Product Viewed
        params:
         user_profile_id - User ID in which we need to add product
         product_id - Product Id which we need to mark viewed
    """
    product_viewed_data, _ = ProductsViewed.objects.get_or_create(user_profile_id=user_profile_id,
                                                                  is_active=True,
                                                                  defaults={"user_profile_id": user_profile_id})
    product_viewed_data.products_viewed.add(product_id)


def get_followings(request):
    """
        Get Following Object based on user id
        params:-
            request:- Request Object
        return:- Following Object
    """
    user_id = request.GET.get("user_id")
    if not user_id:
        return {"error": "User Id should be provided"}, 400
    following_data = Following.objects.filter(user_profile_id=user_id, is_active=True).first()
    return following_data, 200
