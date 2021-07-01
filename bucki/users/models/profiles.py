"""
Profile model.
"""

# Django
from django.db import models

# Utilities
from bucki.utils.models import BuckiModel

class Profile(BuckiModel):
    """
    Profile model.

    A Profile holds the user's public data such as picture, biography and statistics.
    """

    user = models.OneToOneField(
        'users.User',
        on_delete = models.CASCADE
    )
    
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=255, blank=True)
    
    # Statistics
    buckets_owned = models.IntegerField(
        default = 0,
        help_text='Buckets owned by the user.'
    )

    buckets_participating = models.IntegerField(
        default = 0,
        help_text='Buckets in which the user participates.'
    )

    def __str__(self):
        """Return user's string representation."""
        return self.username    
