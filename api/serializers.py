from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Salon

def create(self, validated_data):
    return User.objects.create_user(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
    
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'
        read_only_fields = ['address']