from rest_framework import serializers
from .models import Post, Tag, Category, Author


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    tags_set = serializers.StringRelatedField(many=True, read_only=True)
    author_inf = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ("id",
                  "slug",
                  "title",
                  "subtitle",
                  "creation_date",
                  "updated_date",
                  "publish_date",
                  "meta_description",
                  "teaser",
                  "body",
                  "published",
                  "author",
                  "cover",
                  "tags",
                  'tags_set',
                  'author_inf',
                  "category")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("id",
                  "name")


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

