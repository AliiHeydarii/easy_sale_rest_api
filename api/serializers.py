from rest_framework import serializers
from .models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id' , 'title' , 'price' , 'description']
        