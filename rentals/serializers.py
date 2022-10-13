from rest_framework import serializers
from .models import Place, Position, Record, CurrentSearchPlace, FavoritePlace

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('latitude','longitude')

class PlaceSerializer(serializers.ModelSerializer):
    position= PositionSerializer()
    class Meta:
        model = Place
        fields = '__all__'
        
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields= '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields= '__all__'

class SearchPlaceSerializer(serializers.ModelSerializer):
    search_place = PlaceSerializer()
    class Meta:
        model = CurrentSearchPlace
        fields= ('id','search_place')

class FavoritePlaceSerializer(serializers.ModelSerializer):
    favorite_place = PlaceSerializer()
    class Meta:
        model = FavoritePlace
        fields = ('id','favorite_place')