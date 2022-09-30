from rest_framework import serializers
from .models import Place, Position, Record

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['latitude','longitude']

class PlaceSerializer(serializers.ModelSerializer):
    position= PositionSerializer()
    class Meta:
        model = Place
        fields = '__all__'
        
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields= '__all__'