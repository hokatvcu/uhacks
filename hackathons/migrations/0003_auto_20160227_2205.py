# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0002_auto_20160227_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hackathon',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='hackathon',
            name='school',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
