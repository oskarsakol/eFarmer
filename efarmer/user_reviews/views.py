from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins

from efarmer.user_reviews.models import UserReviews
from .serializers import UserReviewSerializer

User = get_user_model()


class UserReviewsViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    """
    Updates and retrieves user_reviews object
    """
    queryset = UserReviews.objects.all()
    serializer_class = UserReviewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
