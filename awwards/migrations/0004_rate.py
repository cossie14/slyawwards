# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-08 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0003_auto_20190906_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=30)),
                ('usability', models.CharField(max_length=8)),
                ('score', models.FloatField(max_length=8)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='awwards.Project')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]