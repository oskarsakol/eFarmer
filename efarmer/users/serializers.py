import re

from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'address', 'city')
        read_only_fields = ('username',)


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

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
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone',
                  'address', 'city')
        extra_kwargs = {'password': {'write_only': True}}
