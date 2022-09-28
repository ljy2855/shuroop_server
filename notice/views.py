from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notice.models import Notification
from notice.serializers import NoticeSerializer

from users.models import Profile

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_notices(request):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        notices = Notification.objects.filter(profile_id=profile)
        serializers = NoticeSerializer(notices,many = True)
        return Response(serializers.data,status=200)
    return Response(status=401)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_all_notices(request):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        Notification.objects.filter(profile_id=profile).delete()
        return Response(status=200)
    return Response(status=401)     

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_notice(request):
    user = request.user
    if user is not None:
        notice_id = request.data['id']
        get_object_or_404(Notification,id=notice_id).delete()
        return Response(status=200)
    return Response(status=401)     

# Create your views here.
