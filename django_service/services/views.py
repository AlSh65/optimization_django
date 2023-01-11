from django.db.models import Prefetch
from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet

from services.serializers import SubscriptionSerializer
from clients.models import Client
from .models import Subscription


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.prefetch_related(
        'plan',
        Prefetch('client',
                 queryset=Client.objects.all().select_related('user').only('company_name',
                                                                           'user__email'))
    )
    serializer_class = SubscriptionSerializer
