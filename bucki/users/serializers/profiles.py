"""
Profile serializer.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/serializers/
"""

# Django REST Framework
from rest_framework import serializers

# Models
from bucki.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """
    Profile model serializer.
    """
    
    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'biography',
            'buckets_owned',
            'buckets_participating'
        )
        read_only_fields = (
            'buckets_owned',
            'buckets_participating'
        )
