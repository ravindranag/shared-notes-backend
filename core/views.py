from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer


class HomeView(APIView):    
    def get(self, request, *args, **kwargs):
        return Response('[Shared Notes]: Server running')