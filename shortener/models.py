from django.db import models
import uuid


class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper()
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
