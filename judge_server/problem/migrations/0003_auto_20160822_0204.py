# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 02:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_machine'),
        ('client', '0001_initial'),
        ('problem', '0002_auto_20160821_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('judge_time', models.DateTimeField(auto_now=True)),
                ('code_length', models.IntegerField()),
                ('user', models.CharField(max_length=64)),
                ('contest', models.CharField(max_length=128, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionCode',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='code', serialize=False, to='problem.Submission')),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionDetail',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='detail', serialize=False, to='problem.Submission')),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionMessage',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='message', serialize=False, to='problem.Submission')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='client.Client'),
        ),
        migrations.AddField(
            model_name='submission',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='judge.Environment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='problem.Problem'),
        ),
    ]