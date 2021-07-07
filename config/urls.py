"""
Bucki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('bucki.users.urls', 'users'), namespace='users')),
    path('', include(('bucki.buckets.urls', 'buckets'), namespace='buckets')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
