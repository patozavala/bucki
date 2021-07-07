"""Bucket URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import buckets as bucket_views

router = DefaultRouter()
router.register(r'buckets', bucket_views.BucketViewSet, basename='bucket')

urlpatterns = [
    path('', include(router.urls))
]