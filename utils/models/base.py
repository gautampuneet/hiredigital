# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    """
        base model which will be inherit by each model
    """

    is_active = models.BooleanField(
        "Is Active",
        default=True)
    created_at = models.DateTimeField(
        'Created At',
        default=datetime.utcnow())
    updated_at = models.DateTimeField(
        "Updated At",
        default=datetime.utcnow())
    is_deleted = models.BooleanField(
        "Is Deleted",
        default=False)

    class Meta:
        abstract = True

    def mark_deleted(self):
        self.is_deleted = True

