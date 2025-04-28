import pytest

from blog.models import Article, Author, NavPage, Tag


@pytest.fixture
def author():
    """
    Fixture to create an author for the tests.
    """
    return Author.objects.create(name="Author")


@pytest.fixture
def article(author):
    """
    Fixture to create an article for the tests.
    """
    return Article.objects.create(
        slug="slug", title="Title", content="Content", author=author
    )


@pytest.fixture
def article2(author):
    """
    Fixture to create an article for the tests.
    """
    return Article.objects.create(
        slug="slug2", title="Title 2", content="Content 2", author=author
    )


@pytest.fixture
def tag():
    return Tag.objects.create(slug="tag", name="Tag")


@pytest.fixture
def tag2():
    return Tag.objects.create(slug="tag2", name="Tag 2")


@pytest.fixture
def nav_page():
    """
    Fixture to create a nav page for the tests.
    """
    return NavPage.objects.create(slug="slug", title="Title", content="Content")
