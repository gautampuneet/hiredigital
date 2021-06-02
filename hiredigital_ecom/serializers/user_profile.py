# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from hiredigital_ecom.models.user_profile import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
        User Profile Serializer
    """
    class Meta:
        model = UserProfile
        fields = ["id", "name"]
