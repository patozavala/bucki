"""
Users URLs.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/ref/urls/
https://www.django-rest-framework.org/api-guide/routers/
"""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from bucki.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
