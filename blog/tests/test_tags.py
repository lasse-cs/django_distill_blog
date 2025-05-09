import pytest
from blog.models import NavPage
from blog.templatetags.blog_tags import nav_bar, markdown
from django.utils.safestring import SafeData


@pytest.fixture
def nav_pages(transactional_db):
    """
    Fixture to create nav pages for testing.
    """
    return [
        NavPage.objects.create(slug=f"page-{i}", title=f"Page {i}", content="Content")
        for i in range(5)
    ]


def test_nav_tag_adds_nav_pages_to_context(nav_pages):
    nav_bar_context = nav_bar()
    assert list(nav_bar_context["pages"]) == nav_pages


def test_markdown_filter():
    """
    Test the markdown filter.
    """

    text = "This is **bold** and this is *italic*."
    expected_html = "<p>This is <strong>bold</strong> and this is <em>italic</em>.</p>"
    assert str(markdown(text)) == expected_html


def test_markdown_filter_gives_safe_string():
    text = "This is **bold**."
    assert isinstance(markdown(text), SafeData)
