# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from hiredigital_ecom.serializers.products import ProductSerializer
from hiredigital_ecom.usecases.products import *


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def products_listview(request):
    if request.method == "GET":
        products_list, status_code = get_products(request)
        serialize_data = ProductSerializer(products_list, many=True).data
        return JsonResponse(serialize_data, status=status_code, safe=False)
    else:
        response, status_code = create_product(request)
        if status_code != 201:
            return JsonResponse(response, status=status_code)
        serialize_data = ProductSerializer(response, many=False).data
        return JsonResponse(serialize_data, status=status_code, safe=False)


@csrf_exempt
@require_http_methods(["GET", 'PUT'])
def products_view(request, product_id):
    """
        1. Get All Active Products and Get Products by iD
        2. Update Product
        params:-
            request:- Request Object
            product_id:- Product for which we have to fetch or update product
        return - Product Json(List/Object)
    """
    if not product_id:
        return JsonResponse({"error": "Product id is not provided"}, 400)
    if request.method == "GET":
        response, status_code = get_products(request, product_id)
        if status_code != 200:
            return JsonResponse(response, status=status_code)
        else:
            serialize_data = ProductSerializer(response, many=False).data
            return JsonResponse(serialize_data, status=200, safe=False)
    else:
        response, status_code = update_product(request, product_id)
        if status_code != 204:
            return JsonResponse(response, status=status_code)
        serialize_data = ProductSerializer(response, many=False).data
        return JsonResponse(serialize_data, status=status_code, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def recommend_products(request):
    """
        Get Recommend Product List
        params:-
            request- Request Object
        return- Products Json(list)
    """
    response, status_code = get_recommend_products(request)
    if status_code != 200:
        return JsonResponse(response, status=status_code)
    else:
        serialize_data = ProductSerializer(response, many=True).data
        return JsonResponse(serialize_data, status=200, safe=False)
