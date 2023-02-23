from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
)


from django.contrib.auth.models import User
from .models import UserProfile

from .serializers import UserSerializer
from .serializers import UserProfileSerializer


@api_view(['POST'])
def user_registration(request):
    try:
        data = request.data
        email = data.get('email')
        username = data.get('username')
        first_name = data.get('full_name')
        password = data.get('password')

        user_object = User.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            is_staff=True
        )
        user_object.set_password(password)
        user_object.save()
        return Response(status=HTTP_200_OK)
        
    except Exception as error:
        return Response(status=HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_user_profile(request, user_id):
    try:
        user_profile_object = UserProfile.objects.get(user=user_id)
        serializer = UserProfileSerializer(user_profile_object, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
# @parser_classes([MultiPartParser, FormParser])
def update_user_profile(request):
    try:
        user = request.user
        user_profile_object = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(instance=user_profile_object, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK)
    
    except Exception as error:
        return Response(status=HTTP_400_BAD_REQUEST)
