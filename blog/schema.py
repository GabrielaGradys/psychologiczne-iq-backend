import graphene
from django.contrib.auth import get_user_model
from django.db.models import Q
from graphene_django import DjangoObjectType
from django.contrib.contenttypes.models import ContentType as DjangoContentType

import blogPosts.schema
from . import models


class ContentType(DjangoObjectType):
    class Meta:
        model = DjangoContentType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    published_posts = graphene.List(PostType)
    related_posts = graphene.List(PostType, slug=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, value=graphene.String())
    posts_by_category = graphene.List(PostType, value=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_published_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(published=True)
        )

    def resolve_related_posts(root, info, slug):
        orginal_tags = [i['tags__name'] for i in models.Post.objects.filter(slug=slug).prefetch_related('tags').values('tags__name')]
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(published=True)
            .filter(~Q(slug=slug))
            .filter(tags__name__in=orginal_tags)
            .distinct()[:3]
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .prefetch_related("grade")
            .filter(published=True)
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(published=True)
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, value):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(published=True)
            .filter(tags__name__iexact=value)[:3]
        )

    def resolve_posts_by_category(root, info, value):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(published=True)
            .filter(category__name__iexact=value)[:3]
        )


schema = graphene.Schema(query=Query)
