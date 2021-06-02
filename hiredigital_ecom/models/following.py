from django.db import models

from utils.models.base import BaseModel
from hiredigital_ecom.models.user_profile import UserProfile


class Following(BaseModel):
    """
        following model
    """
    user_profile = models.ForeignKey(UserProfile, related_name="user_profile", on_delete=models.CASCADE)

    following = models.ManyToManyField(UserProfile, related_name="following", blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Following'
        verbose_name_plural = 'Followings'

    def __str__(self):
        return self.user_profile.name
