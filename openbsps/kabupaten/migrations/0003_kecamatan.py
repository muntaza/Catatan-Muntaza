# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kabupaten', '0002_auto_20170827_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('nama_kecamatan', models.CharField(db_column='nama_kecamatan', max_length=200, verbose_name='Kecamatan')),
                ('id_provinsi', models.ForeignKey(db_column='id_provinsi', on_delete=django.db.models.deletion.CASCADE, to='kabupaten.Provinsi', verbose_name='Provinsi')),
            ],
            options={
                'db_table': 'kecamatan',
                'verbose_name': 'Kecamatan',
                'verbose_name_plural': 'Kecamatan',
            },
        ),
    ]
