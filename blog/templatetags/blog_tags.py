from blog.models import NavPage
from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()


@register.inclusion_tag("blog/tags/nav.html")
def nav_bar():
    """
    Custom template tag to add the navbar.
    """
    pages = NavPage.objects.all()
    return {"pages": pages}


@register.filter(name="markdown")
def markdown(text):
    return mark_safe(md.markdown(text))
