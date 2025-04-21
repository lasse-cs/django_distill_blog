from django_distill import distill_path
from blog import views
from blog.models import Article


def get_all_articles():
    """
    Function to get all articles for distillation.
    This function is used to generate static files for all articles.
    """
    for article in Article.objects.all():
        yield {"article_id": article.id}


urlpatterns = [
    distill_path("", views.index, name="index", distill_file="index.html"),
    distill_path(
        "article/<int:article_id>.html",
        views.article,
        name="article",
        distill_func=get_all_articles,
    ),
]
