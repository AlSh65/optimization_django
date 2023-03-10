from celery import shared_task
from django.db.models import F
from celery_singleton import Singleton

@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription
    subscription = Subscription.objects.filter(id=subscription_id).annotate(annotated_price=(
            F('service__full_price') -
            F('service__full_price') * F('plan__discount_percent') / 100)).first()
    new_price = subscription.service.full_price - \
                (subscription.service.full_price * subscription.plan.discount_percent / 100)
    subscription.price = subscription.annotated_price
    subscription.save()

    # .annotate(price=(F('service__full_price') -

    #                   F('service__full_price') * F('plan__discount_percent') / 100))
