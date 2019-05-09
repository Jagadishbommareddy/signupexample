from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name')

class SignupSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    email = serializers.EmailField()
    class Meta:
        model = Signup
        fields = ('id', 'user','email')