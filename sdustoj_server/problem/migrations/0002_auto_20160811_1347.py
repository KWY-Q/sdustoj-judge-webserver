# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='in_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='out_size',
            field=models.IntegerField(default=0),
        ),
    ]