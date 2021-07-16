"""
Bucket membership viewset.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/viewsets/
"""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Bucki
from bucki.buckets.models import Bucket, Membership
from bucki.buckets.serializers import MembershipModelSerializer
from bucki.buckets.permissions.memberships import IsActiveBucketMember

class MembershipViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """Bucket membership viewset."""

    serializer_class= MembershipModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the bucket exists."""
        slug_name = kwargs['slug_name']
        self.bucket = get_object_or_404(Bucket, slug_name=slug_name)
        return super().dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action != 'create':
            permissions.append(IsActiveBucketMember)
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Retrieves the bucket active members."""
        members = Membership.objects.filter(
            bucket=self.bucket,
            is_active=True
        )
        return members
    
    def get_object(self):
        """Return the bucket member by using the user's username."""
        return get_object_or_404(
            Membership,
            user__username=self.kwargs['pk'],
            bucket=self.bucket,
            is_active=True
        )

    def perform_destroy(self, instance):
        """Disable the membership."""
        instance.is_active = False
        instance.save()
