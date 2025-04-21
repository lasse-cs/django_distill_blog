from django.db import models
from django.urls import reverse


class Article(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("article", args=[self.slug])
