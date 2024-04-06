import uuid

from django.db import models
from order.choices import OrderStatus
from person.models import Person
from event.models import Event, Ticket


class DiscountCoupon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255, unique=True)
    percentage = models.IntegerField()
    expiration_date = models.DateField()
    producer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='discount_coupons')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='discount_coupons')
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.IntegerField(OrderStatus, default=OrderStatus.awaiting)
    customer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='orders')
    discount_coupon = models.ForeignKey(DiscountCoupon, on_delete=models.CASCADE, related_name='orders')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment')
    created_at = models.DateTimeField(auto_now_add=True)
