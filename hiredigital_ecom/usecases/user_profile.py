# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from hiredigital_ecom.models.user_profile import UserProfile
from hiredigital_ecom.models.following import Following
from hiredigital_ecom.models.products_viewed import ProductsViewed


def login_user(request):
    """
        Get User Data Based on Name
        params:-
            request:- Request object
        response:- User Profile Object
    """
    name = request.GET.get("name")
    if not name:
        return {"error": "Please provide a valid name"}, 400
    user_data = UserProfile.objects.filter(name__iexact=name)
    if not user_data.exists():
        return {"message": "No User exist with this name, Please provide correct name or create user"}, 400
    return user_data.first(), 200


def create_user(request):
    """
        Create User
        params:-
            request:- Request Object
        response:- Create User Data
    """
    request_data = json.loads(request.body)
    name = request_data.get("name", "")
    if not name:
        return {"error": "Please provide a valid name"}, 400
    user = UserProfile.objects.filter(name__iexact=name)
    if user.exists():
        return {"message": 'User with this name already exist'}, 400
    email = request_data.get("email", "")
    number = request_data.get("number", "")
    user_data_dict = dict()
    user_data_dict["name"] = name
    user_data_dict["email"] = email
    user_data_dict["phone_number"] = number
    user_data = UserProfile.objects.create(**user_data_dict)
    Following.objects.create(user_profile_id=user_data.id)
    ProductsViewed.objects.create(user_profile_id=user_data.id)

    return user_data, 201


def get_users_list():
    """
        Get All Active Users List
        response:- Users Object
    """
    user_data = UserProfile.objects.filter(is_active=True)
    return user_data, 200
