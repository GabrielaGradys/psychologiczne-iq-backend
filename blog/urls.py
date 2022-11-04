from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet, CategoryViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'blog_posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path("", include(router.urls))
]