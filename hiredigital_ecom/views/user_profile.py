# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from hiredigital_ecom.usecases.user_profile import *
from hiredigital_ecom.serializers.user_profile import UserProfileSerializer


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    """
        1. Get User Based on name
        2. Create User
        params:-
            request:- Request Object
            return:- User Profile Json(object)
    """
    if request.method == "GET":
        response, status_code = login_user(request)
        if status_code != 200:
            return JsonResponse(response, status=status_code)
        serialize_data = UserProfileSerializer(response, many=False).data
        return JsonResponse(serialize_data, status=status_code, safe=False)
    else:
        response, status_code = create_user(request)
        if status_code != 201:
            return JsonResponse(response, status=status_code)
        serialize_data = UserProfileSerializer(response, many=False).data
        return JsonResponse(serialize_data, status=status_code, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def get_users(request):
    """
        Get ALL Active Users
        params:-
            request:- Request Object
        return:- User Profile Json(List)
    """
    response, status_code = get_users_list()
    if status_code != 200:
        return JsonResponse(response, status=status_code)
    serialize_data = UserProfileSerializer(response, many=True).data
    return JsonResponse(serialize_data, status=status_code, safe=False)
