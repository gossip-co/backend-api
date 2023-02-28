from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED,
    HTTP_201_CREATED, HTTP_302_FOUND,
)
from django.contrib.auth.models import User
from group.models import Group
from .models import Subscription
from .serializers import SubscriptionSerializer


@api_view(['POST'])
def create_subscription(request):
    try:
        user = request.user
        data = request.data
        group_id = data.get('group_id')

        user_object = User.objects.get(pk=user.id)
        group_object = Group.objects.get(pk=group_id)

        """Adding memeber to the group"""
        try:
            try:
                is_user_joined = group_object.members.get(pk=user.id)
                if(is_user_joined):
                    return Response({"error": "User already joind the group"}, status=HTTP_400_BAD_REQUEST)

            except ObjectDoesNotExist:
                group_object.members.add(user_object)
                group_object.total_member = F('total_member') + 1
                group_object.save()

        except Exception as error:
            print(error)
            return Response("Failed adding the subscription", status=HTTP_400_BAD_REQUEST)

        """Creating Subscription"""
        try:
            subscription_object = Subscription.objects.create(
                user=user_object,
                group=group_object
            )
            subscription_object.save()
            return Response(status=HTTP_201_CREATED)
        except Exception as error:
            return Response("Faild adding the subscription in the subscription list", status=HTTP_400_BAD_REQUEST)

    except Exception as error:
        print(error)
        return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cancel_subscription(request):
    try:
        user = request.user
        data = request.data
        group_id = data.get('group_id')
        subscription_id = data.get('subscription_id')

        user_object = User.objects.get(pk=user.id)
        group_object = Group.objects.get(pk=group_id)
        subscription_object = Subscription.objects.get(pk=subscription_id)
        if(subscription_object.user!=user):
            return Response(status=HTTP_401_UNAUTHORIZED)

        """Removing memeber to the group"""
        try:
            group_object.members.remove(user_object)
            group_object.total_member = F('total_member') - 1
            group_object.save()

        except Exception as error:
            print(error)
            return Response("Failed removing the subscription", status=HTTP_400_BAD_REQUEST)

        """Removing Subscription"""
        try:
            subscription_object.delete()
            return Response(status=HTTP_200_OK)

        except Exception as error:
            return Response("Faild remove the subscription in the subscription list", status=HTTP_400_BAD_REQUEST)

    except Exception as error:
        print(error)
        return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def subscriptions(request):
    try:
        user = request.user
        subscription_object = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subscription_object, many=True)
        return Response(serializer.data, status=HTTP_302_FOUND)
    except Exception as error:
        return Response(status=HTTP_400_BAD_REQUEST)