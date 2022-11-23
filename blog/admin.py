from django.contrib import admin

from .models import Author, Post, Tag, Category
from blogPosts.models import Paragraph
from blogPosts.admin import ElementsInline, GradeInline
import nested_admin


@admin.register(Author)
class ProfileAdmin(admin.ModelAdmin):
    model = Author
    list_display = (
        "user",
        "website",
        "bio",
    )
    list_editable = (
        "website",
        "bio",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = (
        "id",
        "name",
        "description",
    )
    list_editable = (
        "name",
        "description",
    )
    search_fields = (
        "name",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = (
        "name",
        "description",
    )
    list_editable = (
        "description",
    )
    search_fields = (
        "name",
    )


class ParagraphInline(nested_admin.NestedStackedInline):
    model = Paragraph
    inlines = [ElementsInline]
    extra = 1


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
        "title",
        "subtitle",
        'category',
        "published",
        "publish_date",
    )
    list_filter = (
        "published",
        "tags",
        "category",
        "publish_date",
        "author",
    )
    list_editable = (
        "subtitle",
        "category",
        "published",
        "publish_date"
    )
    search_fields = (
        "title",
        "subtitle",
    )
    date_hierarchy = "publish_date"
    save_on_top = True
