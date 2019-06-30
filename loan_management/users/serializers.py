from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'id_external',
            'name',
            'registry_code',
            'phone',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'email',
            'id_external',
            'name',
            'registry_code',
            'phone',
            'created_at',
            'updated_at',
        )
