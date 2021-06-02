from django.db import models

from utils.models.base import BaseModel

from hiredigital_ecom.models.user_profile import UserProfile
from hiredigital_ecom.models.product import Products


class ProductsViewed(BaseModel):
    """
        Product Viewed Model
    """
    user_profile = models.ForeignKey(UserProfile, related_name="products_viewed_profile", on_delete=models.CASCADE)
    products_viewed = models.ManyToManyField(
        Products,
        related_name="products_viewed",
        default=[],
        blank=True
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'ProductViewed'
        verbose_name_plural = 'ProductsViewed'

    def __str__(self):
        return self.user_profile.name
