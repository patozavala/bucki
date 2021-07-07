"""
Bucket permissions.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/permissions/
"""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from bucki.buckets.models.memberships import Membership

class IsBucketAdmin(BasePermission):
    """Allow access only to bucket admins."""

    def has_object_permission(self, request, view, obj):
        """Verify user have a membership in the obj."""
        try:
            Membership.objects.get(
                user=request.user,
                bucket=obj,
                is_admin=True,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True