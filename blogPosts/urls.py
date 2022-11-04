from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElementViewSet, ParagraphViewSet, TextWithImageViewSet, \
    GradeViewSet

router = DefaultRouter()
router.register(r'paragraphs', ParagraphViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'textswithiamge', TextWithImageViewSet)
router.register(r'grades', GradeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]