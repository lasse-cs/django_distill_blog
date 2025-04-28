import pytest
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_index_view_uses_correct_template(client):
    """
    Test that the index view can be reached.
    """
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/index.html")
    assertTemplateUsed(response, "blog/tags/nav.html")


def test_index_view_has_all_articles_in_context(client, articles):
    """
    Test that the index view has all articles in its context.
    """

    response = client.get("/")
    assert "articles" in response.context
    assert len(response.context["articles"]) == len(articles)
    for article in articles:
        assert article in response.context["articles"]


def test_article_view_uses_correct_template(client, article):
    """
    Test that the article view can be reached.
    """
    response = client.get(article.get_absolute_url())
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/article.html")
    assertTemplateUsed(response, "blog/tags/nav.html")


def test_article_view_passes_article_to_template(client, article):
    """
    Test that the article view passes the correct article to the template.
    """
    response = client.get(article.get_absolute_url())
    assert "article" in response.context
    assert response.context["article"] == article


def test_nav_view_uses_correct_templates(client, nav_page):
    """
    Test that the nav view can be reached.
    """
    response = client.get(nav_page.get_absolute_url())
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/nav_page.html")
    assertTemplateUsed(response, "blog/tags/nav.html")


def test_nav_view_passes_nav_page_to_template(client, nav_page):
    """
    Test that the nav view passes the correct nav page to the template.
    """
    response = client.get(nav_page.get_absolute_url())
    assert "page" in response.context
    assert response.context["page"] == nav_page


def test_tag_view_uses_correct_template(client, tag):
    """
    Test that the tag view can be reached.
    """
    response = client.get(tag.get_absolute_url())
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/tag.html")
    assertTemplateUsed(response, "blog/tags/nav.html")


def test_tag_view_passes_tag_to_template(client, tag):
    """
    Test that the tag view passes the correct tag to the template.
    """
    response = client.get(tag.get_absolute_url())
    assert "tag" in response.context
    assert response.context["tag"] == tag
