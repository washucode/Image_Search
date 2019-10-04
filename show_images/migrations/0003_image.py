# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-04 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_images', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image_category', models.ManyToManyField(to='show_images.Category')),
                ('location_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_images.location')),
            ],
        ),
    ]
