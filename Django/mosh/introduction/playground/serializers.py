from djoser.serializer import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
class UserCreateSerializer(BaseUserCreateSerializer):
    ''' This serializer will be used for user's authentication and djoser customization '''
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']