"""
Users models admin.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Bucki
from bucki.users.models import User, Profile

class BuckiUserAdmin(UserAdmin):
    """
    User model admin.
    """
    list_display = ('email', 'username', 'is_staff', 'is_client')

    list_filter = ('is_client', 'is_staff', 'created', 'modified')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile admin.
    """
    list_display = ('user', 'buckets_owned', 'buckets_participating')
    search_fields = ('user__username', 'user__email', 'user__is_verified', 'user__date_joined')
    list_filter = ('buckets_owned', 'user__date_joined')
    
# Model is registered into Django's admin interface.
admin.site.register(User, BuckiUserAdmin)
