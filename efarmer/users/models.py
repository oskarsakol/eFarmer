import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return self.username
