from playwright.sync_api import expect


def test_index_page(page, server_url, distill):
    page.goto(server_url)
    expect(page).to_have_title("Test Title")
