# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OSPaperInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.IntegerField(default=0)),
                ('stu_name', models.CharField(max_length=20)),
                ('paper_name', models.CharField(max_length=200)),
            ],
        ),
    ]