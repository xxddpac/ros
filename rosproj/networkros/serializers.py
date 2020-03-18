from rest_framework import serializers
from .models import User
from .models import DeviceManage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeviceManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceManage
        fields = '__all__'