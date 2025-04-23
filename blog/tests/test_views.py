import pytest
from pytest_django.asserts import assertTemplateUsed
from blog.models import Article

pytestmark = pytest.mark.django_db


def test_index_view_uses_correct_template(client):
    """
    Test that the index view can be reached.
    """
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/index.html")


def test_index_view_has_all_articles_in_context(client, articles):
    """
    Test that the index view has all articles in its context.
    """

    response = client.get("/")
    assert "articles" in response.context
    assert len(response.context["articles"]) == len(articles)
    for article in articles:
        assert article in response.context["articles"]


def test_article_view_uses_correct_template(client):
    """
    Test that the article view can be reached.
    """
    article = Article.objects.create(slug="slug", title="Title", content="Content")
    response = client.get(article.get_absolute_url())
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/article.html")


def test_article_view_passes_article_to_template(client):
    """
    Test that the article view passes the correct article to the template.
    """
    article = Article.objects.create(slug="slug", title="Title", content="Content")
    response = client.get(article.get_absolute_url())
    assert "article" in response.context
    assert response.context["article"] == article
