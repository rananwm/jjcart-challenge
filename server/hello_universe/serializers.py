from rest_framework import serializers

class HelloUniverseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)