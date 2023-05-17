from rest_framework import serializers
from .models import Note
from users.models import User
from users.serializers import UserSerializer

class NoteOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class NoteListSerializer(serializers.ModelSerializer):
    owner = NoteOwnerSerializer()
        
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner']
