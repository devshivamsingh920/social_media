from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated




class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




    
class LoginAPIView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Login successful",

                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },

                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                }

            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Invalid username or password"
        }, status=status.HTTP_401_UNAUTHORIZED)

    

class ProfileAPIView(APIView):

      permission_classes = [IsAuthenticated]

      def get(self, request):

        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "message": "Profile fetched successfully"
        })



class UpdateProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        user = request.user

        username = request.data.get('username')
        email = request.data.get('email')

        if username:
            user.username = username

        if email:
            user.email = email

        user.save()

        return Response({
            "message": "Profile updated successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_200_OK)
