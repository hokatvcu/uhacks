# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0003_auto_20160227_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='pastDue',
            field=models.BooleanField(default=True),
        ),
    ]
