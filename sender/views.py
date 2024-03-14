from .models import Receiver
from .serializers import ReceiverSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ReceiverView(APIView):
    def get(self, request):
        receivers = Receiver.objects.all()
        serializer = ReceiverSerializer(
            receivers, many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceiverSerializer(data=request.data)
        if serializer.is_valid():
            receiver = serializer.save()
            phone = "213"+receiver.phonenumber
            url = "http://localhost:3333/api/sendText"  # Replace with your actual API endpoint

            # Prepare the data to be sent in the request body (replace with your data structure)
            data = {
                "chatId": phone,
                "text": "this is a test message",
                "session": "default"
            }
            # Set headers (optional, add headers if your API requires them)
            headers = {
                "Content-Type": "application/json"  # Example header for JSON data
            }

            # Send the POST request
            response = requests.post(url, json=data, headers=headers)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
