from django.contrib import admin
from .models import Plan, Service, Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'plan')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'discount_percent')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_price')
