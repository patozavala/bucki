"""
Bucket admin.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
"""

# Django
from django.contrib import admin

# Models
from bucki.buckets.models import Bucket

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    """
    Representation of the Bucket model in the Django's admin interface.
    """
    
    list_display= (
        'name',
        'slug_name',
        'is_public',
        'is_limited',
        'members_limit'
    )
    search_fields = (
        'name',
        'slug_name',
    )
    list_filter = ('is_public',)