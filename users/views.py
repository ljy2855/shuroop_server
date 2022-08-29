from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from users.serializers import ProfileSerializer

from .models import Profile

#패스워드 로그인
@api_view(['POST'])
def login_with_password(request):
    try:
        id = request.data['email']
        pwd = request.data['password']
        
        user = authenticate(username=id, password=pwd)
        
        token,created= Token.objects.get_or_create(user=user)
        print(token)
        return Response({'token' : token.key} ,status=200)

    except AttributeError:
        return Response(status=404)

#토큰으로 유저 정보 받아오기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def check_token(request):
    user = request.user
    if user is not None:
        profile = get_object_or_404(Profile,user_id=user)
        profile_serializer = ProfileSerializer(profile)
        return Response(profile_serializer.data,status=200)
    else:
        return Response(status=404)

#회원가입
@api_view(['POST'])
def sign_up(request):
    try:
        username=request.data['email']
        password=request.data['password']
        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token' : token.key} ,status=200)

    except AttributeError:
        return Response(status=404)

#아이디 존재 여부 확인
@api_view(['POST'])
def check_id(request):
    id = request.data['email']
    get_object_or_404(User,username=id)
    return Response(status=200)

# class LoginView(APIView):
#     def post(self, request):
#         
#         if user is None:
#             token = Token.objects.get(user=user)
# Create your views here.
