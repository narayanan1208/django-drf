from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "Invalid Credentials"}, status=400)

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie("jwt", str(refresh.access_token), httponly=True)
        response.data = {"message": "Login successful"}
        return response


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print("User:", request.user)
        print("Is authenticated:", request.user.is_authenticated)

        return Response(UserSerializer(user).data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "Logged out"}
        return response
