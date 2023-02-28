from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED,
    HTTP_201_CREATED,
)

from .models import Group
from .serializers import GroupSerializer

@api_view(['GET'])
def groups(request):
    try:
        group_obj = Group.objects.all()
        serializer = GroupSerializer(group_obj, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    except Exception as error:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_group(request):
    try:
        user = request.user
        data  = request.data
        name = data.get('name')
        group_object = Group.objects.create(
            admin=user,
            name=name
        )
        group_object.save()
        return Response(status=HTTP_201_CREATED)
    except Exception as error:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def edit_group_detail(request):
    try:
        user = request.user
        group_object = Group.objects.get(admin=user)
        if(group_object.admin!=user): #shall be removed while refactoring ??
            return Response(HTTP_401_UNAUTHORIZED)
        serializer = GroupSerializer(instance=group_object, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)


# For M.V.P we don't need query because group_unique_code is slug_filed which is unique so we can, simple get this by .get method 
# is_lauched should be True , or return 404
@api_view(['GET'])
def search_group(request, group_slug):
    try:
        group_object = Group.objects.get(slug=group_slug)
        if not group_object.is_launched:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = GroupSerializer(group_object, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

# current user, 
@api_view(['GET'])
def is_group_created_by_user(request):
    try:
        user = request.user
        group_object = Group.objects.get(admin=user)
        if(group_object.admin!=user): #shall be removed while refactoring ??
            return Response(status=HTTP_401_UNAUTHORIZED)
        serializer = GroupSerializer(group_object, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
