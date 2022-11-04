from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ckeditor.fields import RichTextField

from blog.models import Post


class Paragraph(models.Model):
    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=500, blank=True)
    rich_text = RichTextField(blank=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='body',
        related_query_name='body',
        to_field='title'
    )

    def __str__(self):
        return self.title


class TextWithImage(models.Model):
    POSITIONS = [
        ('UP', 'up'),
        ('DO', 'down'),
        ('LE', 'left'),
        ('RI', 'right'),
    ]
    image = models.FileField(blank=True)
    rich_text = RichTextField()
    image_position = models.CharField(choices=POSITIONS, max_length=2, blank=True)
    elements = models.ForeignKey(
        'Element',
        blank=True,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f'{self.id}'


class Grade(models.Model):
    tag = models.CharField(max_length=300, null=True)
    book_cover = models.FileField()
    general = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    readability = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    valence = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    credibility = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    knowledge = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    post = models.OneToOneField(
        Post,
        on_delete=models.PROTECT,
        related_name='grade',
        related_query_name='grade',
    )

    def __str__(self):
        return f'{self.tag if self.tag else self.id}'


class Element(models.Model):
    limit = models.Q(app_label='blogPosts') & ~models.Q(
        model__startswith='element') & ~models.Q(
        model='paragraph') & ~models.Q(model='grade')
    name = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
        null=True,
    )
    paragraphs = models.ForeignKey(
        'Paragraph',
        on_delete=models.CASCADE,
        related_name='element',
        related_query_name='element',
        blank=True,
    )

    def __str__(self):
        return f'{self.id}'
