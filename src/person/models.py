import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from person.choices import PersonRole


class PersonManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        person = self.model(email=email, *args, **kwargs)
        person.set_password(password)
        person.save()
        return person

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('role', 0)
        return self.create_user(email, password, *args, **kwargs)


class Person(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    document = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    role = models.IntegerField(choices=PersonRole, default=PersonRole.customer)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PersonManager()

    def __str__(self):
        return self.email
