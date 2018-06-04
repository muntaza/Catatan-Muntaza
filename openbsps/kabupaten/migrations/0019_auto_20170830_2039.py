# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kabupaten', '0018_penduduk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penerima',
            fields=[
                ('id_penduduk', models.OneToOneField(db_column='id_penduduk', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='kabupaten.Penduduk')),
            ],
            options={
                'db_table': 'penerima',
                'verbose_name': 'Penerima',
                'verbose_name_plural': 'Penerima',
            },
        ),
        migrations.CreateModel(
            name='Tahun',
            fields=[
                ('tahun', models.SmallIntegerField(db_column='tahun', primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['tahun'],
                'db_table': 'tahun',
                'verbose_name': 'Tahun',
                'verbose_name_plural': 'Tahun',
            },
        ),
        migrations.AddField(
            model_name='penerima',
            name='tahun',
            field=models.ForeignKey(db_column='tahun', on_delete=django.db.models.deletion.CASCADE, to='kabupaten.Tahun', verbose_name='Tahun'),
        ),
    ]