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

    BucketModel extends from BuckiModel and acts as the abstract base class from which every specialized bucket must inherit.

    Each custom bucket must be implemented into a separate app and designed to hold specific data types in an ordered and structured way. 
    The fields of the specialized bucket model are stored in an independent table in the database. 

    Implementation of custom buckets

    Every custom bucket model must incorporate at least the following fields to ensure the integrity and scalability of the database.
        
    'members': Refers to the users who can participate in the bucket. It is recommended to represent as a ManyToManyField through Invitations.

    'is_limited': A boolean indicates if the bucket has a maximum number of integrants who can participate.

    'members_limit': If a bucket is limited, this will be the limit on the number of members.


    Additionally, a class that holds the specific data must be created. This class must inherit from BuckiModel and should have at least a field that collects the data.

    '<your_custom_bucket_data>': Represent the data that is stored in the bucket. This field must hold the data in the most ordered and structured way and be related to the bucket through a ForeignKey field.

    Example: 
    
    imbucket - Application for storing images

    # imbucket/models/imagebuckets.py

    from bucki.utils.buckets import Bucket

    class ImBucket(Bucket):

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

    # imbucket/images.py

    from bucki.utils.models import BuckiModel
    from django.db import models

    class ImData(BuckiModel):

        image = models.ImageField(
            upload_to='custom_path/'
        )


    Finally, the app must be installed in config/settings/base.py and registered in the /bucki/imbucket/app.py file.
    """

    name = models.CharField('Bucket name', max_length=140)
    
    slug_name = models.SlugField(unique=True, max_length=40)
    
    description = models.CharField('Bucket description', max_length=255)
    
    tags = TaggableManager()
    
    is_public = models.BooleanField(
        default=True,
        help_text='Public buckets are listed in the main page so everyone know about their existence.'
    )

    class Meta(BuckiModel.Meta):
        abstract = True
