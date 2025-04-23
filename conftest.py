import pytest

from blog.models import Article, NavPage


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
def about_page(transactional_db):
    return NavPage.objects.create(
        slug="about",
        title="About",
        content="This is the about page.",
    )
