from django.db import models


class TicketType(models.IntegerChoices):
    adult = 0
    concession = 1
