"""
MSBucket model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

# Django
from django.db import models

# Bucki
from bucki.utils.buckets import Bucket

class MSBucket(Bucket):
    """
    MSBucket is specially designed to hold multispectral data.

    Multispectral data is assumed disgregated in several files representing channels input by the client. 'MSData' class stores the data into a single structured file in the database join with enriched metadata. 'MSData' has a ManyToOne relationship with MSBucket.
    """

    members = models.ManyToManyField(
        'users.User',
        through='multispectral.Membership',
        through_fields=('bucket', 'user')
    )

    is_limited = models.BooleanField(
        'Is limited',
        default=False,
        help_text='Limited buckets can grow up to a fixed number of members.'
    )

    members_limit = models.PositiveIntegerField(
        'Members limit',
        default=0,
        help_text='If a bucket is limited, this will be the limit on the number of members.'
    )

    def __str__(self):
        """Return the name of the bucket."""
        return self.name



