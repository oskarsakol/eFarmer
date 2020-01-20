from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from efarmer.advertisements.models import Advertisement
from efarmer.users.permissions import IsUserOrReadOnly
from .serializers import AdvertisementSerializer

User = get_user_model()


class AdvertisementViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """
    Updates and retrieves advertisement object
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsUserOrReadOnly,)


class AdvertisementDetailView(LoginRequiredMixin, DetailView):
    model = Advertisement
    slug_field = "name"
    slug_url_kwarg = "name"