# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 23:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabupaten', '0009_auto_20170828_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penduduk',
            name='no_ktp',
            field=models.CharField(db_column='no_ktp', max_length=16, validators=[django.core.validators.MinLengthValidator(16, message='Cek No. KTP')], verbose_name='No KTP'),
        ),
    ]
