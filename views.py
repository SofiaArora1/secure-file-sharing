from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from .models import User, File
from .serializers import UserSerializer, FileSerializer
from django.conf import settings
from itsdangerous import URLSafeSerializer

# Serializer for generating encrypted URLs
s = URLSafeSerializer(settings.SECRET_KEY)

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UploadFileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.user_type != 'OPS':
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploader=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 'CLIENT':
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

class DownloadFileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if request.user.user_type != 'CLIENT':
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        try:
            file = File.objects.get(pk=pk)
            encrypted_url = s.dumps(file.file.url)
            return Response({"download-link": encrypted_url, "message": "success"})
        except File.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
