# Generated by Django 5.0.2 on 2024-02-24 13:01

import Gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to=Gallery.models.GalleryPic)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]