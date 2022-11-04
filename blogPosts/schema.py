from graphene_django import DjangoObjectType

from . import models


class ParagraphType(DjangoObjectType):
    class Meta:
        model = models.Paragraph


class ElementType(DjangoObjectType):
    class Meta:
        model = models.Element


class TextWithImageType(DjangoObjectType):
    class Meta:
        model = models.TextWithImage


class GradeType(DjangoObjectType):
    class Meta:
        model = models.Grade

