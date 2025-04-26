from django.shortcuts import render
from blog.models import Article, NavPage, Tag


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})


def article(request, slug):
    article = Article.objects.get(pk=slug)
    return render(request, "blog/article.html", {"article": article})


def tag(request, slug):
    tag = Tag.objects.get(pk=slug)
    return render(request, "blog/tag.html", {"tag": tag})


def nav_page(request, slug):
    nav_page = NavPage.objects.get(pk=slug)
    return render(request, "blog/nav_page.html", {"page": nav_page})
