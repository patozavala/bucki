"""
Bucket viewset

For more information on this file, see
https://www.django-rest-framework.org/api-guide/viewsets/
"""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

# Models
from bucki.buckets.models.buckets import Bucket
from bucki.buckets.models.memberships import Membership

# Serializer
from bucki.buckets.serializers import BucketModelSerializer

# Permissions
from bucki.buckets.permissions.buckets import IsBucketAdmin

class BucketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Bucket view set."""

    serializer_class = BucketModelSerializer
    lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Bucket.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    
    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsBucketAdmin)
        return [permission() for permission in permissions]
        
    def perform_create(self, serializer):
        """Assign bucket admin."""
        bucket = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            bucket=bucket,
            is_admin=True,
            remaining_invitations=8
        )
