# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20180130_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]