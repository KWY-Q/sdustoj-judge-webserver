# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0009_auto_20160827_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvalidWord',
            fields=[
                ('creator', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=30)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invalid_word', to='problem.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]