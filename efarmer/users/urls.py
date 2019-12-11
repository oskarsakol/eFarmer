from django.urls import path

from efarmer.users.views import (
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("<str:username>/", view=user_detail_view, name="detail"),
]
