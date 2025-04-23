import re
from playwright.sync_api import expect


def test_index_page(page, server_url, articles):
    # There is a great new blog in town
    # L goes to visit it:
    page.goto(server_url)

    # He notices that it has Blog in the title
    expect(page).to_have_title(re.compile("Blog"))

    # He is also notices that there is a showing that this lists the articles
    title = page.get_by_role("heading", name="All Articles")
    expect(title).to_be_visible()

    # There is a list of articles
    article_list = page.get_by_role("article")
    expect(article_list).to_have_count(len(articles))
    for article in articles:
        # Each article has a title
        title = article_list.get_by_role("heading", name=article.title)
        expect(title).to_be_visible()

        # Each article has a content
        content = article_list.get_by_text(article.content)
        expect(content).to_be_visible()

        # Each article has a link to the article
        link = article_list.get_by_role("link", name=article.title)
        expect(link).to_be_visible()

    # Clicking on the title of an article takes him to a dedicated page for the
    # article
    first_article = articles[0]
    article_link = page.get_by_role("link", name=first_article.title)
    article_link.click()

    # The article page has the title of the article
    expect(page).to_have_title(re.compile(first_article.title))
    title = page.get_by_role("heading", name=first_article.title)
    expect(title).to_be_visible()

    # The article page has the content of the article
    content = page.get_by_text(first_article.content)
    expect(content).to_be_visible()

    # There is a navbar
    navbar = page.get_by_role("navigation", name="Main Navigation")
    expect(navbar).to_be_visible()

    # With a link to the index page
    index_link = navbar.get_by_role("link", name="Blog")
    index_link.click()

    # The index page has the title of the blog
    expect(page).to_have_title(re.compile("Blog"))
    title = page.get_by_role("heading", name="Articles")


def test_main_navigation(page, server_url, about_page):
    # L goes to visit the blog
    page.goto(server_url)

    # He is on the main index page
    expect(page).to_have_title(re.compile("Blog"))
    title = page.get_by_role("heading", name="All Articles")
    expect(title).to_be_visible()

    # He sees there is a navbar at the top of the page
    navbar = page.get_by_role("navigation", name="Main Navigation")
    expect(navbar).to_be_visible()

    # The navbar has a link to the index page
    index_link = navbar.get_by_role("link", name="Blog")
    expect(index_link).to_be_visible()

    # The navbar also has a link to an about page
    about_link = navbar.get_by_role("link", name="About")
    expect(about_link).to_be_visible()
    about_link.click()

    # He is taken to the about page
    expect(page).to_have_title(re.compile("About"))
    title = page.get_by_role("heading", name="About")
    expect(title).to_be_visible()

    # The about page still has the navbar
    navbar = page.get_by_role("navigation", name="Main Navigation")
    expect(navbar).to_be_visible()

    # The navbar has a link to the index page
    index_link = navbar.get_by_role("link", name="Blog")
    expect(index_link).to_be_visible()
    index_link.click()

    # He is taken back to the index page
    expect(page).to_have_title(re.compile("Blog"))
    title = page.get_by_role("heading", name="All Articles")
    expect(title).to_be_visible()
