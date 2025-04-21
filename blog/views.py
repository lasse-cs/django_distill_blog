from django.shortcuts import render
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})


def article(request, slug):
    article = Article.objects.get(pk=slug)
    return render(request, "blog/article.html", {"article": article})
