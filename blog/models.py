from django.db import models
from django.urls import reverse


class Page(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Article(Page):
    tags = models.ManyToManyField("Tag", blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("article", args=[self.slug])

    def __str__(self):
        return f"{self.title} - {self.author.name}"


class NavPage(Page):
    def get_absolute_url(self):
        return reverse("nav_page", args=[self.slug])

    def __str__(self):
        return self.title


class Tag(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("tag", args=[self.slug])

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
