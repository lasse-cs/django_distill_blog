import pytest
from blog.models import NavPage
from blog.templatetags.blog_tags import nav_bar


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
