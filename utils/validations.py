# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hiredigital_ecom.models.user_profile import UserProfile
from hiredigital_ecom.models.product import Products


def validate_stock(stock):
    if stock in [True, False]:
        return True
    return False


def validate_user_profile(user_profile):
    return UserProfile.objects.filter(pk=user_profile)


def validate_price(price):
    if type(price) not in [int, float]:
        return False
    return True


def validate_following(following):
    if type(following) != list:
        return False
    profiles_count = UserProfile.objects.filter(pk__in=following).values("name").count()
    if profiles_count != len(following):
        return False
    return True


def validate_products(products):
    if type(products) != list:
        return False
    profiles_count = Products.objects.filter(pk__in=products).values("name").count()
    if profiles_count != len(products):
        return False
    return True
