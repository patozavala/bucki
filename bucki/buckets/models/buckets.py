"""
Bucket model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

# Django
from django.db import models

# Utilities
from bucki.utils.models import BuckiModel
from taggit.managers import TaggableManager


class Bucket(BuckiModel):
    """
    Bucket model.

    BucketModel extends from BuckiModel. Buckets are designed for holding specific data files in an ordered and structured way. 
    
    The specialized files are stored in an independent table in the database.
    """

    name = models.CharField('Bucket name', max_length=140)
    
    slug_name = models.SlugField(unique=True, max_length=40)
    
    description = models.CharField('Bucket description', max_length=255)
    
    tags = TaggableManager()
    
    is_public = models.BooleanField(
        default=True,
        help_text='Public buckets are listed in the main page so everyone know about their existence.'
    )

    members = models.ManyToManyField(
        'users.User',
        through='buckets.Membership',
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

    # Statistics
    bucket_size = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the name of the bucket."""
        return self.name

    class Meta(BuckiModel.Meta):
        """Meta class."""
        ordering = ['-bucket_size']
