from django.db import models


class OrderStatus(models.IntegerChoices):
    awaiting = 0
    concluded = 1
    canceled = 2
