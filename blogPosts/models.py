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

    class Meta:
        ordering = ["id"]

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


class Button(models.Model):
    TYPES = [
        ('File', 'File'),
        ('Link', 'Link'),
    ]
    COLORS = [
        ('pq_yellow', 'Yellow'),
        ('pq_light_blue', 'Light Blue'),
    ]
    type = models.CharField(choices=TYPES, default='File', max_length=4)
    color = models.CharField(choices=COLORS, default='Yellow', max_length=15)
    text = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    file = models.FileField(upload_to='uploads/', blank=True)
    elements = models.ForeignKey(
        'Element',
        blank=True,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f'{self.id}'


class Tab(models.Model):
    COLORS = [
        ('pq_yellow', 'Yellow'),
        ('pq_light_blue', 'Light Blue'),
    ]
    color = models.CharField(choices=COLORS, default='Yellow', max_length=15)
    title = models.CharField(max_length=200)
    icon = models.FileField(blank=True)
    body = RichTextField()
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
    multi_columns = models.BooleanField(default=False)
    paragraphs = models.ForeignKey(
        'Paragraph',
        on_delete=models.CASCADE,
        related_name='element',
        related_query_name='element',
        blank=True,
    )

    def __str__(self):
        return f'{self.id}'
