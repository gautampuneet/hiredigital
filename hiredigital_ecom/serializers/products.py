# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from hiredigital_ecom.models.product import Products
from hiredigital_ecom.serializers.user_profile import UserProfileSerializer
from hiredigital_ecom.serializers.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    """
        Products Serializer
    """
    user_profile = UserProfileSerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Products
        fields = ["id", "name", "image", "stock", "unit_price", "sale_price", "updated_at", "created_at",
                  "user_profile", "category"]
