# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

from utils.models.base import BaseModel
from hiredigital_ecom.models.category import Categories
from hiredigital_ecom.models.user_profile import UserProfile


class Products(BaseModel):
    """
        product models
    """
    user_profile = models.ForeignKey(UserProfile, related_name="product_user", on_delete=models.CASCADE)
    name = models.CharField(
        "Product Name",
        max_length=256
    )

    image = models.CharField(
        "Image",
        max_length=512,
        blank=True
    )

    category = models.ForeignKey(
        Categories,
        related_name="categories",
        on_delete=models.CASCADE
    )

    stock = models.BooleanField(
        "Product Stock",
        default=False
    )

    unit_price = models.FloatField(
        "Unit Price",
        blank=True
    )

    sale_price = models.FloatField(
        "Sale Price",
        blank=True
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
