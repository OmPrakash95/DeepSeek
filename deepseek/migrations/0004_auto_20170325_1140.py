# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-25 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepseek', '0003_auto_20170325_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='process_id',
            field=models.IntegerField(default=0),
        ),
    ]