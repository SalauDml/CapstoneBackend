from django.shortcuts import render
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
# Create your views here.

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = UserSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':"user created successfully "},status=status.HTTP_201_CREATED)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     username = serializer.validated_data.get['username']
        #     password = serializer.validated_data.get['password']
        #     print(username) | "Empty"

        user = authenticate(username=username,password=password)
        

        if user is not None:
            print("User is not none and request received")
            access =  AccessToken.for_user(user)
            return Response({
                'access': str(access),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

