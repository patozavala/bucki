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

    A Profile holds the user's public data such as picture, and statistics.
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
    
    # Statistics
    buckis_owned = models.IntegerField(
        default = 0,
        help_text='Buckis owned by the user.'
        )

    buckis_participating = models.IntegerField(
        default = 0,
        help_text='Buckis in which the user participates.'
        )

    def __str__(self):
        """Return user's string representation."""
        return self.username

    
