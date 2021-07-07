"""
Invitation model.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

# Django
from django.db import models

# Utilities
from bucki.utils.models import BuckiModel

class Invitation(BuckiModel):
    
    class Meta:
        abstract = True