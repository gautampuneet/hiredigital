# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from hiredigital_ecom.usecases.following import update_following, get_followings
from hiredigital_ecom.serializers.following import FollowingSerializer


@csrf_exempt
@require_http_methods(["PUT"])
def UpdateFollowing(request, following_id):
    """
        Update Following Object
        params:
         request - Request Object
         following_id - Following Id which needed to be updated
        return:- Following Json(Object)
    """
    if not following_id:
        return JsonResponse({"error": "Following id is not provided"}, 400)
    response, status_code = update_following(request, following_id)
    if status_code != 204:
        return JsonResponse(response, status=status_code)
    serialize_data = FollowingSerializer(response, many=False).data
    return JsonResponse(serialize_data, status=status_code, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def get_following_by_user(request):
    """
        Get List of Following Based on user id
        params:
        request:- Request object
        return:- Following Json (List)
    """
    response, status_code = get_followings(request)
    if status_code != 200:
        return JsonResponse(response, status=status_code)
    serialize_data = FollowingSerializer(response, many=False).data
    return JsonResponse(serialize_data, status=status_code, safe=False)
