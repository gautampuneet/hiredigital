# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utils.models.base import BaseModel


class UserProfile(BaseModel):
    """
        User Profile Model
    """
    name = models.CharField(
        "Full Name",
        max_length=256
    )

    email = models.EmailField(
        "Email",
        max_length=256,
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        "Phone Number",
        max_length=32,
        null=True,
        blank=True
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.name
