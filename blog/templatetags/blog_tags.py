from blog.models import NavPage
from django import template


register = template.Library()


@register.inclusion_tag("blog/tags/nav.html")
def nav_bar():
    """
    Custom template tag to add the navbar.
    """
    pages = NavPage.objects.all()
    return {"pages": pages}
