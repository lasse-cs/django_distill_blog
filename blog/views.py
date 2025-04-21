from django.shortcuts import render
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "blog/article.html", {"article": article})
