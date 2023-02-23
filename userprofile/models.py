from django.db import models
from django.contrib.auth.models import User

from uuid import uuid4


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET)
    bio = models.CharField(max_length=150, null=True, blank=True)
    profile_pic = models.FileField(null=True, blank=True)
    timeline_pic = models.FileField(null=True, blank=True)
    instagram_username=models.CharField(max_length=20, null=True, blank=True)
    twitter_username=models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) #Refactor, remove `null` before deployment of the production code 
    is_verified = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username