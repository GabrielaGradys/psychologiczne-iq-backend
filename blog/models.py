from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


def get_default_author():
    return Author.objects.get(id=1)


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    # Metadata
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    published = models.BooleanField(default=False)

    title = models.CharField(max_length=120, unique=True)
    subtitle = models.CharField(max_length=400)
    cover = models.FileField()
    teaser = models.TextField()

    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        to_field='name'
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='post_by_tag',
        related_query_name='post_by_tag'
    )
    author = models.ForeignKey('Author', on_delete=models.PROTECT, default=get_default_author)

    def save(self, *args, **kwargs):
        self.slug = f'{f"{self.category}".lower()}/{slugify(self.title)}'
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    def __str_(self):
        return f"Blog Post of title {self.title}"


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.user.username
