from rest_framework import serializers
from .models import Paragraph, Element, TextWithImage, Grade


class ParagraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paragraph
        fields = "__all__"


class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = "__all__"

class TextWithImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextWithImage
        fields = "__all__"

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = "__all__"