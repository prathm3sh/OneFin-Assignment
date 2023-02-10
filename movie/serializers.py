from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    genres = serializers.CharField(max_length=500)
    uuid = serializers.UUIDField()