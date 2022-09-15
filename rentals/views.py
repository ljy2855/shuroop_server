import asyncio
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import get_object_or_404
from devices.signal import borrow_signal, return_signal
from rentals.models import Place
from rentals.serializers import PlaceSerializer
from users.models import Profile

@api_view(['GET'])
def get_all_places(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many= True)
    return Response(serializer.data,status=200)


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

        serializer = PlaceSerializer(place)
        return Response(serializer.data,status=200)
    else:
        return Response(status=404)


 # Create your views here.
