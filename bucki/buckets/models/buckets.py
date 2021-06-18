"""
Bucket model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

# Django
from django.db import models

# Utilities
from bucki.utils.models import BuckiModel


class Bucket(BuckiModel):
    """
    Bucket model.

    Extend from BuckiModel.
    
    Incorpore some extra fields to capture the desired behavior of buckets in different applications.

    Acts as an abstract base class for all especialized buckets.
    """

    name = models.CharField('bucket name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    description = models.CharField('bucket description', max_length=255)

    members = models.ManyToManyField(
        'users.User',
        through='buckets.Membership',
        through_fields=('bucket', 'user')
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public buckets are listed in the main page so everyone know about their existence.'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If bucket is limited, this will be the limit on the number of members.'
    )

    class Meta(BuckiModel.Meta):
        abstract = True
