from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from django.utils.dateparse import parse_datetime

class WebhookView(APIView):
    def post(self, request):
        data = request.data

        conversation_id = data.get('conversation_id')
        message_id = data.get('message_id')
        content = data.get('content')
        sender = data.get('sender')
        timestamp = parse_datetime(data.get('timestamp'))

        if not all([conversation_id, message_id, content, sender, timestamp]):
            return Response({'error': 'Dados incompletos.'}, status=status.HTTP_400_BAD_REQUEST)

        conversation, created = Conversation.objects.get_or_create(external_id=conversation_id)

        Message.objects.update_or_create(
            external_id=message_id,
            defaults={
                'conversation': conversation,
                'content': content,
                'sender': sender,
                'timestamp': timestamp
            }
        )

        return Response({'status': 'Mensagem processada com sucesso.'}, status=status.HTTP_200_OK)
