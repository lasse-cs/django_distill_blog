import pytest
from django.core.exceptions import ValidationError
from blog.models import Article, NavPage, Tag


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


def test_tag_model():
    """
    Test the basic properties of the tag model.
    """
    tag = Tag.objects.create(slug="tag", name="Tag")
    assert tag.slug == "tag"
    assert tag.name == "Tag"


def test_tag_slug_required():
    """
    Test that the tag slug is required
    """
    tag = Tag(slug="", name="Tag")
    with pytest.raises(ValidationError):
        tag.full_clean()


def test_tag_name_required():
    """
    Test that the tag name is required
    """
    tag = Tag(slug="tag", name="")
    with pytest.raises(ValidationError):
        tag.full_clean()


def test_tag_can_tag_multiple_articles():
    """
    Test that a tag can be associated with multiple articles.
    """
    article1 = Article.objects.create(
        slug="slug1", title="Title 1", content="Content 1"
    )
    article2 = Article.objects.create(
        slug="slug2", title="Title 2", content="Content 2"
    )

    tag = Tag.objects.create(slug="tag", name="Tag")

    tag.article_set.add(article1, article2)
    tag.save()

    tag.refresh_from_db()
    assert tag.article_set.count() == 2
    assert article1 in tag.article_set.all()
    assert article2 in tag.article_set.all()


def test_article_can_have_tags():
    """
    Test that an article can have tags.
    """
    article = Article.objects.create(slug="slug", title="Title", content="Content")
    tag1 = Tag.objects.create(slug="tag1", name="Tag 1")
    tag2 = Tag.objects.create(slug="tag2", name="Tag 2")
    article.tags.add(tag1, tag2)
    article.save()

    article.refresh_from_db()
    assert article.tags.count() == 2
    assert tag1 in article.tags.all()
    assert tag2 in article.tags.all()
