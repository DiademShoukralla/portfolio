# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-14 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='street_address',
            field=models.CharField(blank=True, max_length=30, verbose_name='street address'),
        ),
    ]
