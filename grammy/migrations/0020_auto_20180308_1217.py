# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grammy', '0019_auto_20180307_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='naima', on_delete=django.db.models.deletion.CASCADE, to='grammy.User'),
        ),
    ]
