# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0003_auto_20161019_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('n', 'Normal User'), ('o', 'Owner')], default='n', max_length=1),
        ),
    ]
