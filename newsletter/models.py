from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    TOPIC_CHOICES = [
        ("editorial", "Editorial tip / news story"),
        ("corrections", "Correction request"),
        ("advertise", "Advertising inquiry"),
        ("partnerships", "Business partnership"),
        ("support", "General support"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.topic}"