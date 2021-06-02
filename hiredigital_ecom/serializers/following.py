# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from hiredigital_ecom.models.following import Following
from hiredigital_ecom.serializers.user_profile import UserProfileSerializer


class FollowingSerializer(serializers.ModelSerializer):
    """
        Following Serializer
    """
    user_profile = UserProfileSerializer(many=False)
    following = UserProfileSerializer(many=True)

    class Meta:
        model = Following
        fields = ["id", "user_profile", "following"]
