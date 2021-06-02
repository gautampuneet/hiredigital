from django.db import models

from utils.models.base import BaseModel
from hiredigital_ecom.models.user_profile import UserProfile


class Categories(BaseModel):
    """
        product categories model
    """
    user_profile = models.ForeignKey(UserProfile, related_name="category_user", on_delete=models.CASCADE)
    name = models.CharField(
        "Category Name",
        max_length=256
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
