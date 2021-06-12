"""
Django models utilities.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/#model-inheritance
"""

# Django
from django.db import models

class BuckiModel(models.Model):
    """
    BuckiModel acts as an abstract base class from which every model in the project will inherit.
    """
        
    created = models.DateTimeField(
        'created at',
        auto_now_add = True,
        help_text = 'Date time on which the object was created.'
    )
    
    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text = 'Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
