from rest_framework.serializers import ModelSerializer

from .models import Subscription

from group.serializers import UserSerializerWithoutCredentials, GroupSerializer


class SubscriptionSerializer(ModelSerializer):
    user = UserSerializerWithoutCredentials()
    group = GroupSerializer()
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'group', 'created_at']