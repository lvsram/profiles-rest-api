from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    # input with characters length less than 10
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields =('id', 'email', 'name', 'password')
        # password field is only for creating new, but not retrieve for existing.
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }

    # override model for this serializer
    # to make sure password is hashed instead of plain text
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # set user_profile with the logged in user and so can be read only.
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
