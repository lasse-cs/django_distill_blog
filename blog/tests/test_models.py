import pytest
from django.core.exceptions import ValidationError
from blog.models import Article, NavPage


pytestmark = pytest.mark.django_db


def test_article_model():
    """
    Test the basic properties of the article model.
    """
    article = Article.objects.create(slug="slug", title="Title", content="Content")
    assert article.slug == "slug"
    assert article.title == "Title"
    assert article.content == "Content"


def test_article_title_required():
    """
    Test that the article title is required
    """
    article = Article(slug="slug", title="", content="Content")
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_content_required():
    """
    Test that the article content is required
    """
    article = Article(slug="slug", title="Title", content="")
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_slug_required():
    """
    Test that the article slug is required
    """
    article = Article(slug="", title="Title", content="Content")
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_get_absolute_url():
    """
    Test the get_absolute_url method of the article model.
    """
    article = Article.objects.create(slug="slug", title="Title", content="Content")
    assert article.get_absolute_url() == f"/article/{article.slug}.html"


def test_nav_page_model():
    """
    Test the basic properties of the nav page model.
    """
    nav_page = NavPage.objects.create(slug="slug", title="Title", content="Content")
    assert nav_page.slug == "slug"
    assert nav_page.title == "Title"
    assert nav_page.content == "Content"
