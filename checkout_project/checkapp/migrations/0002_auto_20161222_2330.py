# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='checkin_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
