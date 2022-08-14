from ast import mod
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.model):
    profile_of = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    type_of_profile = models.IntegerField(blank=True, null=True) # 1=Teacher 2=Student
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_name)