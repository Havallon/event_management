from django.db import models


class PersonRole(models.IntegerChoices):
    admin = 0
    producer = 1
    customer = 2
