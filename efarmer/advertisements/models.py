from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Advertisement(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True)
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', blank=True)
    date_from = models.DateTimeField(auto_now_add=True, blank=True)
    date_to = models.DateTimeField(null=True, blank=True)
    description = models.CharField(_('description'), max_length=255, blank=True)
    picture = models.FileField()
    price = models.IntegerField()
    delivery_address = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_address',
                                         blank=True)
    views = models.IntegerField()

    def __str__(self):
        return self.name
