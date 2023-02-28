from django.urls import path

from .views import (
    create_group, edit_group_detail,
    search_group, is_group_created_by_user,
    groups
)

urlpatterns = [
    path('create/', create_group, name="create-group"),
    path('list/', groups, name="groups"),
    path('edit/', edit_group_detail, name="edit-group-detail"),
    path('search/<str:group_slug>/', search_group, name="search-group"),
    path('is_created/', is_group_created_by_user, name="is_group_created_by_user")
]
