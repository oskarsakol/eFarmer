from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from efarmer.advertisements.views import AdvertisementViewSet
from efarmer.user_reviews.views import UserReviewsViewSet
from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'advertisements', AdvertisementViewSet)
router.register(r'user_reviews', UserReviewsViewSet)

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
