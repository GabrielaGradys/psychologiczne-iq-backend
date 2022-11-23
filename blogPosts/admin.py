from django.contrib import admin
import nested_admin

from .models import Paragraph, Element, TextWithImage, Grade, Button, Tab


class TextWithImageInline(nested_admin.NestedStackedInline):
    model = TextWithImage
    extra = 0


class ButtonsInline(nested_admin.NestedStackedInline):
    model = Button
    extra = 0


class TabsInline(nested_admin.NestedStackedInline):
    model = Tab
    extra = 0


class ElementsInline(nested_admin.NestedStackedInline):
    model = Element
    inlines = [TextWithImageInline, ButtonsInline, TabsInline]
    extra = 0


class GradeInline(nested_admin.NestedStackedInline):
    model = Grade
    extra = 0


@admin.register(Element)
class ElementAdmin(nested_admin.NestedModelAdmin):
    model = Element
    inlines = [TextWithImageInline, ButtonsInline, TabsInline]
    extra = 0
    list_display = (
        "id",
        "name",
        "multi_columns",
        "paragraphs",
    )


@admin.register(Paragraph)
class ParagraphAdmin(nested_admin.NestedModelAdmin):
    model = Paragraph
    inlines = [ElementsInline]
    extra = 0
    list_display = (
        "title",
        "sub_title",
        "post",
    )


@admin.register(TextWithImage)
class TextWithImageAdmin(admin.ModelAdmin):
    model = TextWithImage
    list_display = (
        "id",
        "image",
        "elements",
    )


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    model = Grade
    list_display = (
        "tag",
        "general",
        "readability",
        "valence",
        "credibility",
        "knowledge",
        "post",
    )
    list_editable = (
        "general",
        "readability",
        "valence",
        "credibility",
        "knowledge",
    )


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    model = Button
    list_display = (
        "id",
        "type",
        "color",
        "link",
        "file",
        "elements",
    )
    list_editable = (
        "type",
        "color",
        "link",
        "file",
    )


@admin.register(Tab)
class TabAdmin(admin.ModelAdmin):
    model = Tab
    list_display = (
        "id",
        "title",
        "icon",
        "color",
        "elements",
    )
    list_editable = (
        "title",
        "icon",
        "color",
    )
