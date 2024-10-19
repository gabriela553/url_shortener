from rest_framework import generics
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny


class ShortenURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer


class RedirectURLView(generics.RetrieveAPIView):
    queryset = ShortenedURL.objects.all()
    lookup_field = "short_code"
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        shortened_url = self.get_object()
        return HttpResponseRedirect(shortened_url.original_url)
