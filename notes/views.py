from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteListSerializer
from rest_framework.response import Response
from users.models import User

# Create your views here.
class NoteListView(APIView):
    def post(self, request, *args, **kwargs):
        owner_id = request.data.get('owner_id')
        
        if not owner_id:
            return Response('Owner Id required.')
        
        serializer = NoteListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner_id=owner_id)
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        notes = Note.objects.all()
        serializer = NoteListSerializer(notes, many=True)
        return Response(serializer.data)