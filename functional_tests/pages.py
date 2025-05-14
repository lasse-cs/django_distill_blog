import re
from playwright.sync_api import expect


class Navbar:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def go_to_index(self):
        index_link = self.locator.get_by_role("link", name="Blog")
        expect(index_link).to_be_visible()
        index_link.click()
        return IndexPage(self.page)

    def go_to_nav_page(self, nav_page):
        nav_page_link = self.locator.get_by_role("link", name=nav_page.title)
        expect(nav_page_link).to_be_visible()
        nav_page_link.click()
        return NavPagePage(self.page)

    def expect_to_be_visible(self):
        expect(self.locator).to_be_visible()


class IndexPage:
    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_role("heading", name="All Articles")

        navbar_locator = page.get_by_role("navigation", name="Main Navigation")
        self.navbar = Navbar(page, navbar_locator)

        article_list_locator = page.get_by_role("main")
        self.article_list = ArticleList(page, article_list_locator)

    def expect_to_have_articles(self, articles):
        self.article_list.expect_to_have_length(len(articles))
        for article in articles:
            self.article_list.expect_to_have_article(article)

    def expect_to_be_loaded(self):
        self.navbar.expect_to_be_visible()
        expect(self.page).to_have_title(re.compile("Blog"))
        expect(self.heading).to_be_visible()

    def visit_article(self, article):
        return self.article_list.visit_article(article)

    def visit_tag_on_article(self, article, tag):
        return self.article_list.visit_tag_on_article(article, tag)

    def get_content_for_article(self, article):
        return self.article_list.get_content_for_article(article)


class TagList:
    def __init__(self, locator):
        self.tag_locators = locator.get_by_role("listitem")

    def expect_to_have_length(self, length):
        expect(self.tag_locators).to_have_count(length)

    def expect_to_have_tag(self, tag):
        tag_link = self.tag_locators.get_by_role("link", name=tag.name)
        expect(tag_link).to_be_visible()

    def expect_to_have_tags(self, tags):
        self.expect_to_have_length(len(tags))
        for tag in tags:
            tag_link = self.tag_locators.get_by_role("link", name=tag.name)
            expect(tag_link).to_be_visible()

    def visit_tag(self, tag):
        tag_link = self.tag_locators.get_by_role("link", name=tag.name)
        tag_link.click()
        return TagPage(tag_link.page)


class TagPage:
    def __init__(self, page):
        self.page = page
        navbar_locator = page.get_by_role("navigation", name="Main Navigation")
        self.navbar = Navbar(page, navbar_locator)

        article_list_locator = page.get_by_role("main")
        self.article_list = ArticleList(page, article_list_locator)

    def expect_to_be_for_tag(self, tag):
        heading = self.page.get_by_role("heading", level=1)
        expect(heading).to_contain_text(tag.name)

        articles = tag.article_set.all()
        self.article_list.expect_to_have_length(len(articles))
        for article in articles:
            self.article_list.expect_to_have_article(article)


class ArticleList:
    def __init__(self, page, locator):
        self.page = page
        self.article_locators = locator.get_by_role("article")

    def expect_to_have_length(self, length):
        expect(self.article_locators).to_have_count(length)

    def _get_article_element(self, article):
        title_locator = self.page.get_by_role("heading", name=article.title)
        return self.article_locators.filter(has=title_locator)

    def expect_to_have_article(self, article):
        article_element = self._get_article_element(article)
        expect(article_element).to_be_visible()

        header_group = article_element.locator("hgroup")
        expect(header_group).to_contain_text(article.author.name)
        expect(header_group).to_contain_text(article.created_at.strftime("%B %d, %Y"))

        article_link = article_element.get_by_role("link", name=article.title)
        expect(article_link).to_be_visible()
        tags_list = TagList(article_element.locator("footer"))
        tags_list.expect_to_have_tags(article.tags.all())

    def visit_article(self, article):
        article_element = self._get_article_element(article)
        article_link = article_element.get_by_role("link", name=article.title)
        article_link.click()

        return ArticlePage(self.page)

    def visit_tag_on_article(self, article, tag):
        article_element = self._get_article_element(article)
        tags = TagList(article_element.locator("footer"))
        return tags.visit_tag(tag)

    def get_content_for_article(self, article):
        article_element = self._get_article_element(article)
        content = article_element.locator("section")
        return content


class ArticlePage:
    def __init__(self, page):
        self.page = page
        self.article_locator = page.get_by_role("article")
        self.header_group = self.article_locator.locator("hgroup")
        self.title = self.header_group.get_by_role("heading")

        navbar_locator = page.get_by_role("navigation", name="Main Navigation")
        self.navbar = Navbar(page, navbar_locator)

        tag_locator = self.article_locator.locator("footer")
        self.tag_list = TagList(tag_locator)

    def expect_to_be_for_article(self, article):
        expect(self.page).to_have_title(re.compile(article.title))
        self.navbar.expect_to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(article.title)

        author = self.header_group.get_by_text(article.author.name)
        expect(author).to_be_visible()

        created_at = self.header_group.get_by_text(
            article.created_at.strftime("%B %d, %Y")
        )
        expect(created_at).to_be_visible()

        self.tag_list.expect_to_have_tags(article.tags.all())

    def get_article_content(self):
        content = self.article_locator.locator("section")
        return content

    def visit_tag(self, tag):
        return self.tag_list.visit_tag(tag)


class NavPagePage:
    def __init__(self, page):
        self.page = page
        nav_bar_locator = page.get_by_role("navigation", name="Main Navigation")
        self.navbar = Navbar(page, nav_bar_locator)

    def expect_to_be_for_nav_page(self, nav_page):
        expect(self.page).to_have_title(re.compile(nav_page.title))
        self.navbar.expect_to_be_visible()

        title = self.page.get_by_role("heading", name=nav_page.title)
        expect(title).to_be_visible()

    def get_page_content(self):
        content = self.page.locator("section")
        return content
