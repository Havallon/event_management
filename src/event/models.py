import uuid

from django.db import models
from event.choices import TicketType
from person.models import Person


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    producer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def file_path(instance, filename):
        return f'media/events/{instance.id}/{filename}'

    banner = models.ImageField(upload_to=file_path)


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section_type = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sections')
    created_at = models.DateTimeField(auto_now_add=True)


class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.IntegerField()
    expiration_date = models.DateField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='batches')
    created_at = models.DateTimeField(auto_now_add=True)


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_type = models.IntegerField(TicketType, default=TicketType.adult)
    price = models.IntegerField()
    amount = models.IntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='tickets')
    created_at = models.DateTimeField(auto_now_add=True)
