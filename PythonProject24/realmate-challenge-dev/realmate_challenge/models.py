from django.db import models

class Conversation(models.Model):
    external_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    external_id = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    sender = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
