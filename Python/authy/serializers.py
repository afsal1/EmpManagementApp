from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
import re
from django.contrib.auth import authenticate
from utilities.jwt_handler import get_tokens_for_user





class RegistrationSerializer(serializers.Serializer):

    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.filter(),
                message="email already exist.",
            )
        ],
    )
    password = serializers.CharField(
        write_only=True, required=True
    )
    first_name = serializers.CharField(
        write_only=True, required=True, max_length=15
    )
    last_name = serializers.CharField(
        write_only=True, required=True, max_length=15
    )
    user_role = serializers.CharField(
        write_only=True, required=True, max_length=15
    )

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_role=validated_data["user_role"],
            
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

    def validate(self, attrs):

        if CustomUser.objects.filter(email=attrs.get("email")):
            raise serializers.ValidationError("Email already exists")
        if len(attrs.get(("password"))) < 6:
            raise serializers.ValidationError("Make sure your password is at lest 6 letters")
        elif re.search('[0-9]',attrs.get("password")) is None:
            raise serializers.ValidationError("Make sure your password has a number in it")
        elif re.search('[a-zA-Z]',attrs.get("password")) is None: 
            raise serializers.ValidationError("Make sure your password has a alphabet in it")
        else:
            pass
        return super(RegistrationSerializer, self).validate(attrs)

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "user_role",
        ]
        password = serializers.CharField(
            write_only=True, required=True, validators=[validate_password]
        )

        extr_kwargs = {
            "password": {"write_only": True},
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "Please enter your email.",
        },
    )
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        write_only=True,
        error_messages={
            "blank": "Please enter your password.",
        },
    )
    
    def validate(self, attrs):
        credentials = {
            "email": attrs.get("email").lower(),
            "password": attrs.get("password"),
        }
        if not all(credentials.values()):
            message = "Must include email and password"
            raise serializers.ValidationError(message)

        user = authenticate(**credentials)

        if not user:
            message = "Unable to sign in with provided credentials"
            raise serializers.ValidationError(message)

        tokens = get_tokens_for_user(user)


        return {
            "access_token": tokens.get("access_token"),
            "refresh_token": tokens.get("refresh_token"),
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "user_role":user.user_role,
            "emp_code":user.emp_code
        }


class ViewEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name",
                "user_role", "emp_code"]