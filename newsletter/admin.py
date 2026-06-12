from django.contrib import admin
from .models import Subscriber, ContactMessage


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    ordering = ("-subscribed_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "topic", "message", "created_at")
    list_filter = ("topic", "created_at")
    search_fields = ("name", "email", "message")