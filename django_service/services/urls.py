from django.urls import path
from rest_framework import routers
from .views import SubscriptionView


router = routers.DefaultRouter()
router.register(r'api/subscriptions', SubscriptionView)

urlpatterns = router.urls