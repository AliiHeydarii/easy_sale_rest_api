from rest_framework import serializers
from .models import Advertisement


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id' , 'title' , 'price' , 'description' , 'city' , 'category']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        rep['category'] = instance.category.name
        return rep
        
class AdDetailSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Advertisement
        fields = '__all__'     
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        rep['user'] = instance.user.email
        rep['city'] = instance.city.name
        return rep