# Generated by Django 4.1.2 on 2022-11-24 12:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paragraph',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='element',
            name='multi_columns',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('pq_yellow', 'Yellow'), ('pq_light_blue', 'Light Blue')], default='Yellow', max_length=15)),
                ('title', models.CharField(max_length=200)),
                ('icon', models.FileField(blank=True, upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('elements', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='blogPosts.element')),
            ],
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('File', 'File'), ('Link', 'Link')], default='File', max_length=4)),
                ('color', models.CharField(choices=[('pq_yellow', 'Yellow'), ('pq_light_blue', 'Light Blue')], default='Yellow', max_length=15)),
                ('text', models.CharField(blank=True, max_length=100)),
                ('link', models.URLField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='uploads/')),
                ('elements', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='blogPosts.element')),
            ],
        ),
    ]
