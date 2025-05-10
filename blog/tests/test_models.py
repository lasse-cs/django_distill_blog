import pytest
from django.core.exceptions import ValidationError
from blog.models import Article, Author, NavPage, Tag


pytestmark = pytest.mark.django_db


def test_article_model(author):
    """
    Test the basic properties of the article model.
    """
    article = Article.objects.create(
        slug="slug", title="Title", content="Content", author=author
    )
    assert article.slug == "slug"
    assert article.title == "Title"
    assert article.content == "Content"
    assert article.author == author
    assert article.created_at is not None


def test_article_model_str(article):
    assert str(article) == f"{article.title} - {article.author.name}"


def test_article_title_required(article):
    """
    Test that the article title is required
    """
    article.title = ""
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_content_required(article):
    """
    Test that the article content is required
    """
    article.content = ""
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_slug_required(article):
    """
    Test that the article slug is required
    """
    article.slug = ""
    with pytest.raises(ValidationError):
        article.full_clean()


def test_article_get_absolute_url(article):
    """
    Test the get_absolute_url method of the article model.
    """
    assert article.get_absolute_url() == f"/article/{article.slug}.html"


def test_nav_page_model():
    """
    Test the basic properties of the nav page model.
    """
    nav_page = NavPage.objects.create(slug="slug", title="Title", content="Content")
    assert nav_page.slug == "slug"
    assert nav_page.title == "Title"
    assert nav_page.content == "Content"
    assert nav_page.created_at is not None


def test_nav_page_model_str(nav_page):
    assert str(nav_page) == nav_page.title


def test_tag_model():
    """
    Test the basic properties of the tag model.
    """
    tag = Tag.objects.create(slug="tag", name="Tag")
    assert tag.slug == "tag"
    assert tag.name == "Tag"


def test_tag_model_str(tag):
    assert str(tag) == tag.name


def test_tag_get_absolute_url(tag):
    """
    Test the get_absolute_url method of the tag model.
    """
    assert tag.get_absolute_url() == f"/tag/{tag.slug}.html"


def test_tag_slug_required(tag):
    """
    Test that the tag slug is required
    """
    tag.slug = ""
    with pytest.raises(ValidationError):
        tag.full_clean()


def test_tag_name_required(tag):
    """
    Test that the tag name is required
    """
    tag.name = ""
    with pytest.raises(ValidationError):
        tag.full_clean()


def test_tag_can_tag_multiple_articles(tag, article, article2):
    """
    Test that a tag can be associated with multiple articles.
    """
    tag.article_set.add(article, article2)
    tag.save()

    tag.refresh_from_db()
    assert tag.article_set.count() == 2
    assert article in tag.article_set.all()
    assert article2 in tag.article_set.all()


def test_article_can_have_tags(tag, tag2, article):
    """
    Test that an article can have tags.
    """
    article.tags.add(tag, tag2)
    article.save()

    article.refresh_from_db()
    assert article.tags.count() == 2
    assert tag in article.tags.all()
    assert tag2 in article.tags.all()


def test_author_model():
    """
    Test the basic properties of the author model.
    """
    author = Author.objects.create(name="Author")
    assert author.name == "Author"


def test_author_model_str(author):
    assert str(author) == author.name


def test_author_name_required(author):
    """
    Test that the author name is required
    """
    author.name = ""
    with pytest.raises(ValidationError):
        author.full_clean()
