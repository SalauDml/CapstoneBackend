from rest_framework import serializers
from .models import Properties,PropertyImages


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
    
    def create(self, validated_data):
        return Properties.objects.create(**validated_data)
    
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = '__all__'
