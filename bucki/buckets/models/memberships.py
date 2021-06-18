"""
Memberships model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

# Django
from django.db import models
from django.db.models.deletion import CASCADE

# Utilities
from bucki.utils.models import BuckiModel

class Membership(BuckiModel):
    """
    Membership model.

    A membership is the table that holds the relationship between
    a user and a bucket.
    """
    user = models.ForeignKey('users.User', on_delete=CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=CASCADE)
    
    is_admin = models.BooleanField(
        'bucket admin',
        default=False,
        help_text="Bucket admins can update the bucket's data and manage its members."
    )

    # Invitations
    used_invitations = models.PositiveSmallIntegerField(default=0)
    remaining_invitations = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by'
    )

    # Status
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Only active users are allowed to interact in the bucket.'
    )

    # def __str__(self):
    #     """Return username and bucket."""
    #     return '@{} at #{}'.format(
    #         self.user.username,
    #         self.bucket.slug_name
    #     )

    class Meta:
        abstract = True
