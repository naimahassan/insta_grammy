# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grammy', '0003_auto_20180303_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grammy.User'),
        ),
        migrations.AddField(
            model_name='likes',
            name='likes_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grammy.User'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.TextField(max_length=100),
        ),
    ]
