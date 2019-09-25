from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """
    class Meta:
        model = models.UserProfile
        """ specify the fields of model that we want to manage using the serializer """
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    """ we have to override the create function
    because otherwise it will call default create
    function of model, but instead we want to call
    create_user function else it will save password as
    it is instead of password hash"""

    def create(self, validated_data):
        """ Create and return a new user"""
        user = models.UserProfile.objects.create_user(

            email= validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
