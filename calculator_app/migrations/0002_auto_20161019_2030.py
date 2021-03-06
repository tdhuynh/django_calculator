# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='equation',
        ),
        migrations.AddField(
            model_name='operation',
            name='num1',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='num2',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='sign',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
