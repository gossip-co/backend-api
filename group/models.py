from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from uuid import uuid4


class Group(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    admin = models.OneToOneField(User, on_delete=models.SET)
    name = models.CharField(max_length=20)
    about = models.TextField(null=True, blank=True)
    icon = models.FileField(null=True, blank=True)
    timeline_img = models.FileField(null=True, blank=True)
    intro_video = models.FileField(null=True, blank=True)
    subscription_rate = models.PositiveIntegerField(null=True, blank=True)
    total_member = models.PositiveBigIntegerField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name="group_members", blank=True)
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_launched = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify("gg-" + self.name + "-{}".format(self.id))
        super(Group, self).save(*args, **kwargs)


    def __str__(self):
        return self.name + ' | admin | ' + self.admin.username