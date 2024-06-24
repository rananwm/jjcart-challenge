from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloUniverseSerializer

class HelloUniverseListView(APIView):
    def get(self, request, format=None):
        messages = [{"message": "Hello, universe!"}]
        return Response(messages)

    def post(self, request, format=None):
        serializer = HelloUniverseSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
