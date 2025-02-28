from django.shortcuts import render
import logging

# Create your views here.d
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User  # Assuming you have a User model
from .serializers import UserSerializer, RegisterSerializer  # Create this serializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    logger.info("Register user API called")

    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        logger.info("User registered successfully")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.warning("User registration validation failed: %s", serializer.errors)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get(username)
    password = request.data.get(password)

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)    
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "token_type": "Bearer"
        })
    else:
        return Response({"detail": "Invalid username or password"}, status=401)

    

