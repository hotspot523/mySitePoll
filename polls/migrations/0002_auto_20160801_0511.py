# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
