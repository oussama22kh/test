from .models import Receiver
from .serializers import ReceiverSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from barcode import Code128
import base64
from PIL import Image


class ReceiverView(APIView):

    def post(self, request):
        serializer = ReceiverSerializer(data=request.data)
        if serializer.is_valid():
            receiver = serializer.save()
            send_message(receiver)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def send_message(receiver):
    url = "http://clonewebsite.ddns.net:3000/send-image"  # Replace with your actual API endpoint
    phone = receiver.phonenumber
    # id = receiver.id
    # barcode = Code128("JT3" + str(id))
    # barcode.save(filename="barcode" + str(id))
    # barcodeimg = Image.open("barcode" + str(id)+".svg")
    # barcodeimg.save("barcode_image.png", format="PNG")
    # card = Image.open("card.png")
    # paste_position = (100, 50,100, 50)
    # card.paste(im=barcodeimg, box=paste_position)
    # card.save(".card"+ str(id))
    # Prepare the data to be sent in the request body (replace with your data structure)
    data = {
        "number": phone,
        "message": "Thanks on advance for your attendance ",
        "imagefile": ""
    }
    # Set headers (optional, add headers if your API requires them)
    headers = {
        "Content-Type": "application/json"  # Example header for JSON data
    }

    # Send the POST request
    requests.post(url, json=data, headers=headers)


