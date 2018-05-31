from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# Create your models here.

class Provinsi(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    kode_provinsi = models.CharField("Kode Provinsi", max_length=20,
                    db_column="kode_provinsi")
    nama_provinsi = models.CharField("Nama Provinsi", max_length=200,
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
    kode_kabupaten = models.CharField("Kode Kabupaten", max_length=20,
                    db_column="kode_kabupaten")
    nama_kabupaten = models.CharField("Nama Kabupaten", max_length=200,
                    db_column="nama_kabupaten")

    class Meta:
        db_table = "kabupaten"
        verbose_name = "Kabupaten"
        verbose_name_plural = "Kabupaten"

    def __unicode__(self):
        return self.nama_kabupaten


class LokasiBidang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_kabupaten = models.ForeignKey(Kabupaten, verbose_name="Kabupaten",
                    db_column="id_kabupaten")
    kode_lokasi_bidang = models.CharField("Kode Lokasi Bidang", max_length=20,
                    db_column="kode_lokasi_bidang")
    nama_lokasi_bidang = models.CharField("Nama Lokasi Bidang", max_length=200,
                    db_column="nama_lokasi_bidang")

    class Meta:
        db_table = "lokasi_bidang"
        verbose_name = "Lokasi Bidang"
        verbose_name_plural = "Lokasi Bidang"

    def __unicode__(self):
        return "%s  %s" % (self.kode_lokasi_bidang, self.nama_lokasi_bidang)


class SKPD(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_lokasi_bidang = models.ForeignKey(LokasiBidang,
                    verbose_name="Lokasi Bidang",
                    db_column="id_lokasi_bidang")
    kode_skpd = models.CharField("Kode SKPD", max_length=20,
                    db_column="kode_skpd")
    nama_skpd = models.CharField("Nama SKPD", max_length=200,
                    db_column="nama_skpd")

    class Meta:
        db_table = "skpd"
        verbose_name = "SKPD"
        verbose_name_plural = "SKPD"

    def __unicode__(self):
        return self.nama_skpd



class StatusPegawai(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    status_pegawai = models.CharField("Status Pegawai", max_length=40,
                    db_column="status_pegawai", unique=True)

    class Meta:
        db_table = "status_pegawai"
        verbose_name = "Status Pegawai"
        verbose_name_plural = "Status Pegawai"

    def __unicode__(self):
        return self.status_pegawai



class Pegawai(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    nama_pegawai = models.CharField("Nama Pegawai", max_length=200,
                    db_column="nama_pegawai")
    nip = models.CharField("NIP", max_length=60,
                    db_column="nip")
    pangkat = models.CharField("Pangkat", max_length=60,
                    db_column="pangkat")
    id_status_pegawai = models.ForeignKey(StatusPegawai,
                    verbose_name="Status Pegawai",
                    db_column="id_status_pegawai")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "pegawai"
        verbose_name = "Pegawai"
        verbose_name_plural = "Pegawai"

    def __unicode__(self):
        return self.nama_pegawai



class SPPD(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="No Urut",
                    db_column="id")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")
    no_sppd = models.CharField("No SPPD", max_length=60,
                    db_column="no_sppd")
    id_pegawai = models.ForeignKey(Pegawai,
                    verbose_name="Pegawai",
                    db_column="id_pegawai")
    tanggal_berangkat = models.DateField("Tanggal Berangkat",
                    db_column="tanggal_berangkat")
    tanggal_kembali = models.DateField("Tanggal Kembali",
                    db_column="tanggal_kembali")
    dibayar = models.DecimalField("Dibayar (Rp)",
                    max_digits=15, decimal_places=0, default=0,
                    db_column="dibayar")
    keterangan = models.CharField("Keterangan", max_length=200,
                    db_column="keterangan")

    class Meta:
        db_table = "sppd"
        verbose_name = "SPPD"
        verbose_name_plural = "SPPD"

    def __unicode__(self):
        return "%s" % (self.id)



#class Event(models.Model):
#    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
#    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
#    end_time = models.TimeField(u'Final time', help_text=u'Final time')
#    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
#
#
#
#
#    class Meta:
#        verbose_name = u'Scheduling'
#        verbose_name_plural = u'Scheduling'
#
#    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
#        overlap = False
#        if new_start == fixed_end or new_end == fixed_start:    #edge case
#            overlap = False
#        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
#            overlap = True
#        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
#            overlap = True
#
#        return overlap
#
#    def get_absolute_url(self):
#        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
#        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
#
#    def clean(self):
#        if self.end_time <= self.start_time:
#            raise ValidationError('Ending hour must be after the starting hour')
#
#        events = Event.objects.filter(day=self.day)
#        if events.exists():
#            for event in events:
#                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
#                    raise ValidationError(
#                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
#                            event.start_time) + '-' + str(event.end_time))
