"""
Membership model serializers

For more information on this file, see
https://www.django-rest-framework.org/api-guide/serializers/
"""

# Django REST Framework
from rest_framework import serializers

# Bucki
from bucki.buckets.models import Membership
from bucki.users.serializers import UserModelSerializer

class MembershipModelSerializer(serializers.ModelSerializer):
    """Membership model serializer."""

    user = UserModelSerializer(read_only=True)
    invited_by = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """Meta class."""
        model = Membership
        fields = (
            'user', 'is_admin', 'is_active',
            'used_invitations', 'remaining_invitations',
            'invited_by', 'joined_at'
        )
        read_only_fields = (
            'user',
            'used_invitations',
            'invited_by'
        )