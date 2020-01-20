from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    auction_from = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('auction_from',)
