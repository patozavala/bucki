"""
Bucket permissions classes.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/permissions/
"""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Bucki
from bucki.buckets.models.memberships import Membership

class IsActiveBucketMember(BasePermission):
    """
    Allow access only to bucket members.
    
    Expect that the views implementing this permission
    have a `bucket` attribute assigned.
    """
    def has_permission(self, request, view):
        """Verify that the user is an active member of the bucket."""
        try:
            Membership.objects.get(
                user=request.user,
                bucket=view.bucket,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
