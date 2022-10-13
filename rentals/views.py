import asyncio
import datetime
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import get_object_or_404
from devices.signal import borrow_signal, return_signal
from rentals import serializers
from rentals.models import CurrentSearchPlace, FavoritePlace, Place, Record
from rentals.serializers import FavoritePlaceSerializer, PlaceSerializer, RecordSerializer, SearchPlaceSerializer
from users.models import Profile
from django.db.models import Q

@api_view(['GET'])
def get_all_places(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many= True)
    return Response(serializer.data,status=200)

@api_view(['GET'])
def get_place(request,id):
    place = get_object_or_404(Place,id=id)
    serializer = PlaceSerializer(place)
    return Response(serializer.data, status=200)


#TODO 웹소켓으로 바꿔야 할듯
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def borrow_umbrella(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        place = get_object_or_404(Place,id=id)
        if place.is_empty :
           return Response(status=201, data={'message' : '대여소가 비었어요'})

        #TODO 대여소 디바이스 연동 파트
        
        asyncio.run(borrow_signal(place_id=id))
        #TODO User 정보 업데이트
        place.borrow_item()
        profile.borrow_umbrella()
        #TODO record create
        Record.objects.create(borrow_place=place,user=profile)
        
        serializer = PlaceSerializer(place)
        return Response(serializer.data,status=200)
    else:
        return Response(status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def return_umbrella(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        place = get_object_or_404(Place,id=id)
        if place.is_full :
           return Response(status=201, data={'message' : '대여소가 가득찼아요'})

        asyncio.run(return_signal(place_id=id)) 
        #TODO User 정보 업데이트
        profile.return_umbrella()
        place.return_item()
        record = get_object_or_404(Record,user=profile,is_renting=True)
        record.close_rental(place=place)
        serializer = RecordSerializer(record)
        return Response(serializer.data,status=200)
    else:
        return Response(status=404)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def search_places(request,keyword):
    if keyword is not None:
        places = Place.objects.filter(
            Q(name__icontains=keyword)|
            Q(address__icontains=keyword)
        )
        serializer = PlaceSerializer(places,many=True)
        return Response(serializer.data,status=200)
    return Response(status=201)    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_searched_places(request):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        places = CurrentSearchPlace.objects.filter(user=profile)
        serializer = SearchPlaceSerializer(places,many=True)
        return Response(serializer.data,status=200)
    return Response(status=201)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_favorite_places(request):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        places = FavoritePlace.objects.filter(user=profile)
        serializer = FavoritePlaceSerializer(places,many=True)
        return Response(serializer.data,status=200)
    return Response(status=201)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_favorite_place(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        search_place = get_object_or_404(Place,id=id)
        place, created = FavoritePlace.objects.get_or_create(user=profile, favorite_place=search_place)
        serializer = FavoritePlaceSerializer(place)
        return Response(serializer.data,status=200)
    return Response(status=201)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_searched_place(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        favorite_place = get_object_or_404(Place,id=id)
        place, created = CurrentSearchPlace.objects.get_or_create(user=profile, search_place=favorite_place)
        serializer = SearchPlaceSerializer(place)
        return Response(serializer.data,status=200)
    return Response(status=201)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove_searched_place(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        
        place = get_object_or_404(CurrentSearchPlace,id=id,user=profile).delete()
        return Response(status=200)
    return Response(status=401)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove_favorite_place(request,id):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        
        place = get_object_or_404(FavoritePlace,id=id,user=profile).delete()
        return Response(status=200)
    return Response(status=401)

 # Create your views here.
