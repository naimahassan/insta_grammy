# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grammy', '0013_user_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
    ]
