# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0004_auto_20171113_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='电影评星'),
        ),
    ]
