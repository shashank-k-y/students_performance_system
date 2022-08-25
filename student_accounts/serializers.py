import random
import string
import datetime
from django.contrib.auth.models import User

from rest_framework import serializers

from student_accounts import models


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(
        style={'input_type': 'password'}, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = ['username', "email", 'password', 'password_2']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        if self.validated_data['password_2'] != password:
            raise serializers.ValidationError("Password didn't match")

        user = User.objects.filter(email=email)
        if user.exists():
            raise serializers.ValidationError(
                'User with the given email already exists'
            )

        account = User(username=username, email=email)
        account.set_password(password)
        account.save()
        return account


class StudentDeatilSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Student
        fields = "__all__"
        read_only_fields = ('roll_number', 'division', 'total_score')

    def get_student_name(self, instance):
        return instance.user.username

    @staticmethod
    def get_roll_number(name):
        unique_number = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=3)
        )
        year = datetime.datetime.today().year
        chars_from_name = name[:3]
        return "".join(str(year) + chars_from_name + unique_number)

    def create(self, validated_data):
        name = validated_data['user'].username
        roll_number = self.get_roll_number(name=name)
        validated_data.update(roll_number=roll_number)
        return models.Student.objects.create(**validated_data)
