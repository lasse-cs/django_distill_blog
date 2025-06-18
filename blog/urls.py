from django_distill import distill_path
from blog import views
from blog.models import Article, NavPage, Tag


def get_all_articles():
    """
    Function to get all articles for distillation.
    This function is used to generate static files for all articles.
    """
    for article in Article.objects.all():
        yield {"slug": article.slug}


def get_all_tags():
    """
    Function to get all tags for distillation.
    This function is used to generate static files for all tags.
    """
    for tag in Tag.objects.all():
        yield {"slug": tag.slug}


def get_all_nav_pages():
    """
    Function to get all navigation pages for distillation.
    This function is used to generate static files for all navigation pages.
    """
    for nav_page in NavPage.objects.all():
        yield {"slug": nav_page.slug}


urlpatterns = [
    distill_path("", views.index, name="index"),
    distill_path(
        "article/<slug:slug>.html",
        views.article,
        name="article",
        distill_func=get_all_articles,
    ),
    distill_path(
        "tag/<slug:slug>.html",
        views.tag,
        name="tag",
        distill_func=get_all_tags,
    ),
    distill_path(
        "<slug:slug>.html",
        views.nav_page,
        name="nav_page",
        distill_func=get_all_nav_pages,
    ),
]
