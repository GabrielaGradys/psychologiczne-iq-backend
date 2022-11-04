from django.contrib import admin

from .models import Author, Post, Tag, Category
from blogPosts.models import Paragraph
from blogPosts.admin import ElementsInline, GradeInline
import nested_admin


@admin.register(Author)
class ProfileAdmin(admin.ModelAdmin):
    model = Author


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


class ParagraphInline(nested_admin.NestedStackedInline):
    model = Paragraph
    inlines = [ElementsInline]
    extra = 0


@admin.register(Post)
class PostAdmin(nested_admin.NestedModelAdmin):
    model = Post
    exclude = ('slug', )
    fieldsets = [
        (None, {
            'fields': ['title', 'subtitle', 'cover', 'teaser']
        }),
        ('Metadata', {
            'fields': ['category', 'tags', 'author']
        }),
        ('Publication Data', {
            'classes': ('collapse',),
            'fields': ['published', 'publish_date', 'meta_description']
        })
    ]
    inlines = [GradeInline, ParagraphInline]
    extra = 0
    list_display = (
        "id",
        "title",
        "subtitle",
        "teaser",
        'category',
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
        "tags",
        "category",
        "author"
    )
    list_editable = (
        "title",
        "subtitle",
        "teaser",
        'category',
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "body",
    )
    date_hierarchy = "publish_date"
    save_on_top = True
