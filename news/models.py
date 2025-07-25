from django.db import models
from django.contrib.auth.models import User

class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    summary = models.TextField()
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
