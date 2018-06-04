# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy
from django.core.validators import MinLengthValidator
from django.core.validators import int_list_validator

from django.db import models


class Provinsi(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    nama_provinsi = models.CharField("Provinsi", max_length=200,
                    db_column="nama_provinsi")

    class Meta:
        db_table = "provinsi"
        verbose_name = "Provinsi"
        verbose_name_plural = "Provinsi"

    def __unicode__(self):
        return self.nama_provinsi



class Kabupaten(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_provinsi = models.ForeignKey(Provinsi, verbose_name="Provinsi",
                    db_column="id_provinsi")
    nama_kabupaten = models.CharField("Kabupaten", max_length=200,
                    db_column="nama_kabupaten")

    class Meta:
        db_table = "kabupaten"
        verbose_name = "Kabupaten"
        verbose_name_plural = "Kabupaten"

    def __unicode__(self):
        return self.nama_kabupaten



class Kecamatan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_kabupaten = models.ForeignKey(Kabupaten, verbose_name="Kabupaten",
                    db_column="id_kabupaten")
    nama_kecamatan = models.CharField("Kecamatan", max_length=200,
                    db_column="nama_kecamatan")

    class Meta:
        db_table = "kecamatan"
        verbose_name = "Kecamatan"
        verbose_name_plural = "Kecamatan"

    def __unicode__(self):
        return self.nama_kecamatan



class Desa(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_kecamatan = models.ForeignKey(Kecamatan, verbose_name="Kecamatan",
                    db_column="id_kecamatan")
    nama_desa = models.CharField("Desa", max_length=200,
                    db_column="nama_desa")

    class Meta:
        db_table = "desa"
        verbose_name = "Desa"
        verbose_name_plural = "Desa"

    def __unicode__(self):
        return "%s, Kecamatan %s" % (self.nama_desa, self.id_kecamatan)



class Status(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    status = models.CharField("Status", max_length=40,
                    db_column="status")

    class Meta:
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __unicode__(self):
        return self.status



class RT(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    rt = models.CharField("RT", max_length=5,
                    db_column="rt")

    class Meta:
        db_table = "rt"
        verbose_name = "RT"
        verbose_name_plural = "RT"

    def __unicode__(self):
        return self.rt



class JenisKelamin(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    kode_jenis_kelamin = models.CharField("Kode Jenis Kelamin", max_length=3,
                    db_column="kode_jenis_kelamin")
    jenis_kelamin = models.CharField("Jenis Kelamin", max_length=40,
                    db_column="jenis_kelamin")

    class Meta:
        db_table = "jenis_kelamin"
        verbose_name = "Jenis Kelamin"
        verbose_name_plural = "Jenis Kelamin"

    def __unicode__(self):
        return self.jenis_kelamin



class Penduduk(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    no_ktp = models.CharField("No KTP", max_length=16,
		    validators=[MinLengthValidator(16, message="No KTP Kurang",),
			        int_list_validator(sep='', message="Cek No KTP", code='invalid', allow_negative=False,),
		    ],
		    unique=True,
                    db_column="no_ktp")
    nama = models.CharField("Nama", max_length=200,
                    db_column="nama")
    tempat_lahir = models.CharField("Tempat Lahir", max_length=200,
                    db_column="tempat_lahir")
    tanggal_lahir = models.DateField("Tanggal Lahir", 
                    db_column="tanggal_lahir")
    id_jenis_kelamin = models.ForeignKey(JenisKelamin, verbose_name="Jenis Kelamin",
		    default=1,
                    db_column="id_jenis_kelamin")
    id_desa = models.ForeignKey(Desa, verbose_name="Desa",
                    db_column="id_desa")
    id_rt = models.ForeignKey(RT, verbose_name="RT",
                    db_column="id_rt")
    no_rumah = models.CharField("No Rumah", max_length=10,
		    blank=True, null=True,
                    db_column="no_rumah")
    bantuan = models.DecimalField("Bantuan", 
		    max_digits=15, decimal_places=0, default=0,
                    db_column="bantuan")
    id_status = models.ForeignKey(Status, verbose_name="Status",
		    default=1,
                    db_column="id_status")
    keterangan = models.TextField("Keterangan",
		    blank=True, null=True,
                    db_column="keterangan")

    class Meta:
        db_table = "penduduk"
        verbose_name = "Penduduk"
        verbose_name_plural = "Penduduk"

    def __unicode__(self):
        return self.nama



class Tahun(models.Model):
    tahun = models.SmallIntegerField(primary_key=True, db_column="tahun")

    class Meta:
        db_table = "tahun"
        verbose_name = "Tahun"
        verbose_name_plural = "Tahun"
	ordering = ["tahun",]

    def __unicode__(self):
        return "%i" % (self.tahun)



class Penerima(models.Model):
    id_penduduk = models.OneToOneField(Penduduk, primary_key=True, 
		    db_column="id_penduduk")
    tahun = models.ForeignKey(Tahun, verbose_name="Tahun",
                    db_column="tahun")

    class Meta:
        db_table = "penerima"
        verbose_name = "Penerima"
        verbose_name_plural = "Penerima"

    def __unicode__(self):
        return "%s" % (self.id_penduduk)



# untuk menampung Inline Tahun
class PendudukPenerima(Penduduk):

    class Meta:
        proxy = True
        verbose_name = "Penduduk Penerima"
        verbose_name_plural = "Penduduk Penerima"

    def __unicode__(self):
        return "%s" % (self.nama)
