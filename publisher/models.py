from django.db import models
from django.contrib.auth.models import User


class FileHolder(models.Model):
    file = models.FileField(blank=True, null=True, upload_to='documents')


class UserProfile(models.Model):
    profile_of = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    type_of_profile = models.IntegerField(blank=True, null=True) # 1=Teacher 2=Student
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_name)


class ProjectPublication(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    type_of = models.IntegerField(blank=True, null=True) # 1=project 2=publication
    files = models.ManyToManyField(FileHolder, blank=True, null=True, related_name='files')
    collaborators = models.ManyToManyField(UserProfile, blank=True, null=True, related_name='colaborators')