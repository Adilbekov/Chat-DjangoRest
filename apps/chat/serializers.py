from rest_framework import serializers
from .models import Message, FrontMessage, BackMessage, DataScienceMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'from_user','to_user', 'content')

class FrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontMessage
        fields = '__all__'

class BackSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackMessage
        fields = '__all__'

class DataScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataScienceMessage
        fields = '__all__'