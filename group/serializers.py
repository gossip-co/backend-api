from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Group


# Why we need this and why don;t just use the UserSerializer, because we dont need email field in group-detail-page, it is unnessasry data
class UserSerializerWithoutCredentials(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'username']


class GroupSerializer(ModelSerializer):
    admin =  UserSerializerWithoutCredentials(many=False, read_only=True)
    class Meta:
        model = Group
        fields = [
            'id', 'admin',
            'name', 'about', 'icon', 'timeline_img',
            'intro_video', 'subscription_rate', 'total_member',
            'slug', 'created_at', 'is_launched'
        ]