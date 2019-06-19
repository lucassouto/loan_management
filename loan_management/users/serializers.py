from rest_framework import serializers

from .views import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id_external', 'name', 'registry_code', 'phone')
