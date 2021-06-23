"""
MultiSpectral images serializers.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/serializers/
"""

# Django REST Framework
from rest_framework import serializers

class MSImageModelSerializer(serializers.ModelSerializer):
    pass

class CreateMSImageSerializer(serializers.ModelSerializer):
    """
    Handle the creation of a new multispectral image related to a Bucket.
    Bucket object must be provided in the context.
    """
    pass
