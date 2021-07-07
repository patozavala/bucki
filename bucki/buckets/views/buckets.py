"""
Bucket viewset

For more information on this file, see
https://www.django-rest-framework.org/api-guide/viewsets/
"""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# # Filters
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend

# Models
from bucki.buckets.models.buckets import Bucket
from bucki.buckets.models.memberships import Membership

# Serializer
from bucki.buckets.serializers.buckets import BucketModelSerializer

# Permissions
from bucki.buckets.permissions.buckets import IsBucketAdmin

class BucketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Bucket view set."""
    queryset = Bucket.objects.all()
    serializer_class = BucketModelSerializer
    # filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    # search_fields = ('slug_name', 'name')
    # ordering_fields = ('buckets_offered', 'buckets_taken', 'name', 'created', 'member_limit')
    # ordering = ('-members__count', '-buckets_offered', '-buckets_taken')
    # filter_fields = ('verified', 'is_limited')

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
