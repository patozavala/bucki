# Django
from django.db import models
from django.db.models.deletion import CASCADE

# Utils
from bucki.utils.memberships import Membership


class MSMembership(Membership):
    """
    Membership for MSBucket, inherit from Membership.
    """
    bucket = models.ForeignKey('multispectral.MSBucket', on_delete=CASCADE)


    def __str__(self):
        """Return username and bucket."""
        return '@{} at #{}'.format(
            self.user.username,
            self.bucket.slug_name
        )
