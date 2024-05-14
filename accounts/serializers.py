from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password",
            "is_active"
        )
        
    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data["username"],
            password=validate_data["password"],
            # first_name=validate_data["first_name"],
            # last_name=validate_data["last_name"],
        )
        return user
    
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "is_active",
            "last_login"
        )