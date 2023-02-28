from django.urls import path

from .views import (
    create_subscription, subscriptions,
    cancel_subscription
)

urlpatterns = [
    path('create/', create_subscription, name="create-subscription"),
    path('get/', subscriptions, name="get-subscriptions"),
    path('cancel/', cancel_subscription, name="cancel-subscription")
]
