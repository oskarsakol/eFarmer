from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Advertisement(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', blank=True)
    auction_from = models.DateTimeField(auto_now_add=True, blank=True)
    auction_to = models.DateField(null=True, blank=True)
    description = models.CharField(_('description'), max_length=255, blank=True)
    picture = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=16)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def delivery_address(self):
        """
        :return: combined user address information
        """
        return self.user.address + ' ' + self.user.city + ' ' + self.user.zip_code
