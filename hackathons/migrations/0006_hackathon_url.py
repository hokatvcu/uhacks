# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0005_remove_hackathon_pastdue'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='url',
            field=models.URLField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
