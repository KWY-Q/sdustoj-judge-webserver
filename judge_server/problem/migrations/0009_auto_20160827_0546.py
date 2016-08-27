# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0008_limit_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(default='Pending', max_length=32),
        ),
        migrations.AlterField(
            model_name='submissionmessage',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
