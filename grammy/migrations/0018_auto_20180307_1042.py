# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammy', '0017_auto_20180307_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='user/'),
        ),
    ]
