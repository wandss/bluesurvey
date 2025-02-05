# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20190718_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionresponse',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(blank=True, to='question.OptionResponse'),
        ),
    ]
