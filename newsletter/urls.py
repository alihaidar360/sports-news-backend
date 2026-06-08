from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register("subscribe", SubscriberViewSet)
router.register("contact", ContactMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]