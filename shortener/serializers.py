from rest_framework import serializers
from .models import ShortenedURL
from django.core.validators import URLValidator


class ShortenedURLSerializer(serializers.ModelSerializer):
    original_url = serializers.URLField(validators=[URLValidator()])

    class Meta:
        model = ShortenedURL
        fields = ["id", "original_url", "short_code", "created_at"]
