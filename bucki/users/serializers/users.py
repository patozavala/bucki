"""
Users serializers.

For more information on this file, see
https://www.django-rest-framework.org/api-guide/serializers/
"""

# Django
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import authenticate, password_validation

# Django email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from bucki.users.models import User, Profile

# Serializers
from bucki.users.serializers.profiles import ProfileModelSerializer

# Utilities
import jwt
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'profile'
        )


class UserSignUpSerializer(serializers.Serializer):
    """
    User sign up serializer.

    Handle sign up data validation and user/profile creation.
    """

    # Account
    username = serializers.CharField(
        min_length=3,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Name
    first_name = serializers.CharField(
        min_length=2,
        max_length=30
    )
    last_name = serializers.CharField(
        min_length=2,
        max_length=30
    )
    
    # Password (only digitation validation errors)
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """Check password and password confirmation match."""
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError('Password do not match.')
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False, is_client=True)
        Profile.objects.create(user=user)
        # Confirmation email (should be implemented by using celery)
        self.send_confirmation_email(user)
        return user
    
    def send_confirmation_email(self, user):
        """Send confirmation email to a given user."""
        verification_token = self.generate_verification_token(user)
        subject = 'Welcome @{}!, please verify your account for start using Bucki.'.format(user.username)
        from_email = 'Bucki <noreply@bucki.app>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {
                'token': verification_token,
                'user': user
            }
        )
        message = EmailMultiAlternatives(subject, content, from_email, [user.email])
        message.attach_alternative(content, 'text/html')
        message.send()

    def generate_verification_token(self, user):
        """Create a JWT token that allows to verify an account."""
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'account_verification'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token


class UserLoginSerializer(serializers.Serializer):
    """
    User login serializer.
    
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """Check credentials."""       
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not verified yet.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Create or retrieve a new token for verification."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer by using a token."""
    
    token = serializers.CharField()

    def validate_token(self, data):
        """Check if token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Token has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token.')
        if payload['type'] != 'account_verification':
            raise serializers.ValidationError('Invalid token.')
        self.context['payload'] = payload
        return data
    
    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
