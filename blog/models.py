from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("article", args=[self.id])
