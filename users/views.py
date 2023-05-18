from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


# Create your views here.
class UserView(APIView):
    
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(serializer.data).data, status=201)
        
        return Response(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)
    
    
class UserDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    