import re
from playwright.sync_api import expect


def test_index_page(page, server_url, distill):
    # There is a great new blog in town
    # L goes to visit it:
    page.goto(server_url)

    # He notices that it has Blog in the title
    expect(page).to_have_title(re.compile("Blog"))

    # He is also notices that there is a heading with the name of the blog
    title = page.get_by_role("heading", name="Blog")
    expect(title).to_be_visible()

    # There is a list of articles

    # Each article has a title
    # Each article has a date
    # The title of each article is a link

    # Clicking on the title of an article takes him to a dedicated page for the
    # article

    # The article page has the title of the article
    # The article page has the content of the article
    # The article page has the date of the article
