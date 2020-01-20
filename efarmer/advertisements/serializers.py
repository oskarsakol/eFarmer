import re

from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Advertisement
from django.utils.translation import gettext_lazy as _


class AdvertisementSerializer(serializers.ModelSerializer):

    def validate_phone(self, value):
        """
        Validates phone number of an organization using Regex
        :param value: phone number
        :return: value or raises ValidationError
        """
        pattern = re.compile(r'(^[+0-9]{1,3})*([0-9]{8,15}$)', re.IGNORECASE)
        value = value.replace(" ", "")
        if pattern.match(value) is None:
            raise ValidationError(_('Please insert correct phone number.'))
        return value

    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('name',)
