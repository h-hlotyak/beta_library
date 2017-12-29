# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 20:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('copyright', models.IntegerField(default=2017)),
                ('num_availible', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]