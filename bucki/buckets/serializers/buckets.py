"""
Buckets serializers.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/serializers/
"""

# Django REST Framework
from rest_framework import serializers

# Models
from bucki.buckets.models.buckets import Bucket


class BucketModelSerializer(serializers.ModelSerializer):
    """Bucket model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=4,
        max_value=64
    )
    is_limited = serializers.BooleanField(default=False)
    is_public = serializers.BooleanField(default=True)

    class Meta:
        """Meta class."""
        model = Bucket
        fields = (
            'name', 'slug_name', 'description', 'bucket_size',
            'is_public', 'is_limited', 'members_limit'
        )
        read_only_fields = (
            'is_public', 'verified', 'bucket_size',
        )

    def validate(self, data):
        """Ensure both members_limit and is_limited are present."""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)
        if is_limited ^ bool(members_limit):
            raise serializers.ValidationError('If bucket is limited, a member limit must be provided')
        return data