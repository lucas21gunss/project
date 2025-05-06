from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Conversation, Message

class WebhookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('webhook')
        self.payload = {
            "conversation_id": "conv123",
            "message_id": "msg123",
            "content": "Teste de mensagem",
            "sender": "cliente",
            "timestamp": "2025-05-06T12:00:00Z"
        }

    def test_webhook_post(self):
        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Conversation.objects.count(), 1)
        self.assertEqual(Message.objects.count(), 1)
