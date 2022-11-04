from rest_framework import viewsets


from .serializers import (
    PostSerializer,
    TagSerializer,
    CategorySerializer,
    ProfileSerializer,
)
from .models import Post, Tag, Category, Author


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related("tags").prefetch_related("body").all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Author.objects.all()
