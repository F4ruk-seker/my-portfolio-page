from django.db import models
import uuid


class Message(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.TextField(max_length=50)
    email = models.EmailField()
    Subject = models.CharField(blank=False,max_length=15, choices=(
        ('Business', 'business'),
        ('Freelance ', 'Freelance '),
        ('Help', 'Help'),
        ('Other', 'Other'),
    ))
    message = models.TextField(max_length=1000)

    sender_detail = models.JSONField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
