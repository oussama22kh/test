import rest_framework.serializers as serializers
from rest_framework import status
from rest_framework.response import Response

from .models import Receiver


class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['name', 'phonenumber']
