import pytest

from blog.models import Article


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
