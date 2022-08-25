from django.contrib.auth.models import User

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(
        style={'input_type': 'password'}, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'password_2']

    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        if self.validated_data['password_2'] != password:
            raise serializers.ValidationError("Password didn't match")

        user = User.objects.filter(username=username)
        if user.exists():
            raise serializers.ValidationError(
                f"User with the given name {username} already exists"
            )

        account = User(username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account