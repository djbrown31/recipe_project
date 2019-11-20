from django.db import models
from django.utils import timezone

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.text
