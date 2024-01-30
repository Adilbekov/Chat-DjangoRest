from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth import password_validation

class UserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'age', 'direction')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'direction', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        if attrs['username'] == attrs['password']:
            raise serializers.ValidationError({'username': 'Пароль похоже на имя пользователя'})
        password_validation.validate_password(attrs['password'], self.instance)
        return attrs

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            phone=validate_data['phone'],
            age=validate_data['age'],
            direction=validate_data['direction'],
            password=validate_data['password']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'direction', 'password', 'confirm_password')