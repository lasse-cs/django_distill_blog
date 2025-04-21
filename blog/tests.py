import pytest
from pytest_django.asserts import assertTemplateUsed
from django.core.exceptions import ValidationError
from blog.models import Article


@pytest.mark.django_db
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


@pytest.mark.django_db
def test_article_view_uses_correct_template(client):
    """
    Test that the article view can be reached.
    """
    article = Article.objects.create(title="Title", content="Content")
    response = client.get(article.get_absolute_url())
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/article.html")


@pytest.mark.django_db
def test_article_view_passes_article_to_template(client):
    """
    Test that the article view passes the correct article to the template.
    """
    article = Article.objects.create(title="Title", content="Content")
    response = client.get(article.get_absolute_url())
    assert "article" in response.context
    assert response.context["article"] == article


@pytest.mark.django_db
def test_article_model():
    """
    Test the basic properties of the article model.
    """
    article = Article.objects.create(title="Title", content="Content")
    assert article.title == "Title"
    assert article.content == "Content"


def test_article_title_required():
    """
    Test that the article title is required
    """
    article = Article(title="", content="Content")
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_content_required():
    """
    Test that the article content is required
    """
    article = Article(title="Title", content="")
    with pytest.raises(ValidationError):
        article.full_clean()


@pytest.mark.django_db
def test_article_get_absolute_url():
    """
    Test the get_absolute_url method of the article model.
    """
    article = Article.objects.create(title="Title", content="Content")
    assert article.get_absolute_url() == f"/article/{article.id}.html"
