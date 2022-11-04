# Generated by Django 4.1.2 on 2022-11-02 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0003_rename_textwithimage_element_textwithimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='BookCover',
            new_name='book_cover',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='General',
        ),
        migrations.AddField(
            model_name='grade',
            name='credibility',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='grade',
            name='knowledge',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='grade',
            name='readability',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='grade',
            name='tag',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='valence',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='textwithimage',
            name='tag',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='general',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
