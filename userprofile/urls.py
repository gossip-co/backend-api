from django.urls import path

from .views import (
    user_registration, get_user_profile,
    update_user_profile
)

urlpatterns = [
    path('registration/', user_registration, name="user-registration"),
    path('profile/<int:user_id>/', get_user_profile, name="get-user-profile"),
    path('update-profile/', update_user_profile, name="update-user-profile")
]
