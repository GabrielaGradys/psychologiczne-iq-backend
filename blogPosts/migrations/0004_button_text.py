# Generated by Django 4.1.2 on 2022-11-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0003_alter_paragraph_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]