# Generated by Django 4.1.2 on 2022-11-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0008_alter_grade_post_alter_paragraph_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textwithimage',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='textwithimage',
            name='image_position',
            field=models.CharField(blank=True, choices=[('UP', 'up'), ('DO', 'down'), ('LE', 'left'), ('RI', 'right')], max_length=2),
        ),
    ]
