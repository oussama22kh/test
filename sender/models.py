from django.db import models


class Receiver(models.Model):
    name = models.CharField(max_length=64)
    phonenumber = models.CharField(max_length=16)
