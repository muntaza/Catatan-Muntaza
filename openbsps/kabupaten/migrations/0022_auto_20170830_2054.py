# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabupaten', '0021_auto_20170830_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penduduk',
            name='bantuan',
            field=models.DecimalField(db_column='bantuan', decimal_places=0, default=0, max_digits=15, verbose_name='Bantuan'),
        ),
    ]
