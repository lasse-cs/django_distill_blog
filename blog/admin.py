from django.contrib import admin

from blog.models import Article, Author, NavPage, Tag


class TagInline(admin.StackedInline):
    model = Article.tags.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    exclude = ("tags",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NavPage)
class NavPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
