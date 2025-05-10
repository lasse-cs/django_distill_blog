from playwright.sync_api import expect
import pytest

from functional_tests.pages import ArticleListPage, NavPagePage


pytestmark = pytest.mark.django_db


def test_visit_index_and_article_page(page, server_url, articles):
    # There is a new blog in town
    # L goes to visit it:
    page.goto(server_url)

    # He lands on the list page of articles
    list_page = ArticleListPage(page)
    list_page.expect_to_be_loaded()
    list_page.expect_to_have_articles(articles)

    # He visits the first article
    first_article = articles[0]
    article_page = list_page.visit_article(first_article)
    article_page.expect_to_be_for_article(first_article)

    # From the article page, he can go back to the index page
    list_page = article_page.navbar.go_to_index()
    list_page.expect_to_be_loaded()
    list_page.expect_to_have_articles(articles)


def test_main_navigation(page, server_url, about_page):
    # L goes to visit the blog
    page.goto(server_url)

    # He is on the main index page
    list_page = ArticleListPage(page)
    list_page.expect_to_be_loaded()

    # He can visit the about page through the navbar
    about_page_page = list_page.navbar.go_to_nav_page(about_page)
    about_page_page.expect_to_be_for_nav_page(about_page)

    # He can go back to the index page through the navbar
    list_page = about_page_page.navbar.go_to_index()
    list_page.expect_to_be_loaded()


def test_tags(page, server_url, tagged_articles):
    # L goes to visit the blog page
    page.goto(server_url)

    # He lands on the list page of articles
    list_page = ArticleListPage(page)
    list_page.expect_to_be_loaded()

    # He can click on a tag in the article list
    # and be taken to the tag page
    first_article = tagged_articles[0]
    first_tag = first_article.tags.first()
    tag_page = list_page.visit_tag_on_article(first_article, first_tag)
    tag_page.expect_to_be_for_tag(first_tag)

    # From the tag page, he can go back to the index page
    list_page = tag_page.navbar.go_to_index()
    list_page.expect_to_be_loaded()

    # He can visit an article from the index page
    article_page = list_page.visit_article(first_article)
    article_page.expect_to_be_for_article(first_article)

    # From the article page, he can also visit the tag page
    tag_page = article_page.visit_tag(first_tag)
    tag_page.expect_to_be_for_tag(first_tag)


def test_markdown_article_content(page, server_url, markdown_article):
    page.goto(server_url)

    list_page = ArticleListPage(page)
    list_page.expect_to_be_loaded()
    list_page.expect_to_have_articles([markdown_article])

    # He sees that the articles have markdown
    article_content = list_page.get_content_for_article(markdown_article)
    marked_up = article_content.locator("strong")
    expect(marked_up).to_have_text("markdown")

    # He can also find the marked up content in the article page
    article_page = list_page.visit_article(markdown_article)
    article_page.expect_to_be_for_article(markdown_article)

    article_content = article_page.get_article_content()
    marked_up = article_content.locator("strong")
    expect(marked_up).to_have_text("markdown")


def test_markdown_navpage(page, server_url, about_page):
    # L goes to visit the about page
    page.goto(server_url + about_page.get_absolute_url())

    about_page_page = NavPagePage(page)
    about_page_page.expect_to_be_for_nav_page(about_page)

    # He can find the marked up content in the article
    page_content = about_page_page.get_page_content()
    marked_up = page_content.locator("strong")
    expect(marked_up).to_have_text("markdown")
