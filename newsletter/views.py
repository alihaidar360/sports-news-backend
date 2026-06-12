from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings

from .models import Subscriber, ContactMessage
from .serializers import SubscriberSerializer, ContactMessageSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        send_mail(
            subject=f"New Contact Form: {contact.topic}",
            message=f"""
Name: {contact.name}

Email: {contact.email}

Topic: {contact.topic}

Message:
{contact.message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )