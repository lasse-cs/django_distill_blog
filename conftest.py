import pytest

from blog.models import Article, NavPage, Tag


@pytest.fixture
def articles(transactional_db):
    articles = []
    for i in range(5):
        article = Article.objects.create(
            slug=f"slug-{i}",
            title=f"Article {i}",
            content=f"Content of article {i}",
        )
        articles.append(article)
    return articles


@pytest.fixture
def tags(transactional_db):
    tags = []
    for i in range(2):
        tag = Tag.objects.create(
            slug=f"tag-{i}",
            name=f"Tag {i}",
        )
        tags.append(tag)

    return tags


@pytest.fixture
def tagged_articles(transactional_db, articles, tags):
    for i in range(5):
        article = articles[i]
        if i % 2 == 0:
            article.tags.add(tags[0])
        if i % 3 == 0:
            article.tags.add(tags[1])
        article.save()
        article.refresh_from_db()
    return articles


@pytest.fixture
def about_page(transactional_db):
    return NavPage.objects.create(
        slug="about",
        title="About",
        content="This is the about page.",
    )
