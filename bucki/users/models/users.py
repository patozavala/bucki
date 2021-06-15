"""
Bucki's users model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


# utils
from bucki.utils.models import BuckiModel

class User(BuckiModel, AbstractUser):
    """
    User model.

    Extend from BuckiModel and Django's AbstractUser.
    
    Change the username field to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user has verified its email address.'
    )
    
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username