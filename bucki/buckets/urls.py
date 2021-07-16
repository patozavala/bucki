"""Bucket URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import buckets as bucket_views
from .views import memberships as membership_views

router = DefaultRouter()
router.register(r'buckets', bucket_views.BucketViewSet, basename='bucket')
router.register(
    r'buckets/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    membership_views.MembershipViewSet,
    basename='membership'
)

urlpatterns = [
    path('', include(router.urls))
]