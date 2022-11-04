from rest_framework import viewsets

from .serializers import ParagraphSerializer, ElementSerializer, \
    TextWithImageSerializer, GradeSerializer
from .models import Paragraph, Element, TextWithImage, Grade


class ParagraphViewSet(viewsets.ModelViewSet):
    serializer_class = ParagraphSerializer
    queryset = Paragraph.objects.all()


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()


class TextWithImageViewSet(viewsets.ModelViewSet):
    serializer_class = TextWithImageSerializer
    queryset = TextWithImage.objects.all()


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
