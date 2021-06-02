# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from hiredigital_ecom.models.category import Categories


class CategorySerializer(serializers.ModelSerializer):
    """
        Category Serialize
    """
    class Meta:
        model = Categories
        fields = ["id", "name", "user_profile"]
