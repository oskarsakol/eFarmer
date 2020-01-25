from rest_framework import serializers
from .models import UserReviews


class UserReviewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField()

    class Meta:
        model = UserReviews
        fields = '__all__'
        read_only_fields = ('date_created', 'author', 'author_username')
