from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author', blank=True)
    description = models.CharField(_('description'), max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    stars = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    @property
    def author_username(self):
        """
        :return: combined user fist_name and last_name
        """
        return self.user.username
