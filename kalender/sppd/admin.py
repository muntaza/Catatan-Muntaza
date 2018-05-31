from django.contrib import admin

from sppd.models import Provinsi, Kabupaten, LokasiBidang, SKPD
from sppd.models import StatusPegawai, Pegawai, SPPD

from sppd.forms import DibayarForm


class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ("kode_provinsi", "nama_provinsi")

class KabupatenAdmin(admin.ModelAdmin):
    list_display = ("kode_kabupaten", "nama_kabupaten", "id_provinsi")

class SKPDInline(admin.TabularInline):
    model = SKPD
    extra = 0

class LokasiBidangAdmin(admin.ModelAdmin):
    list_display = ("kode_lokasi_bidang", "nama_lokasi_bidang", "id_kabupaten")
    ordering = ["kode_lokasi_bidang"]
    list_per_page = 10
    inlines = [SKPDInline]


class SKPDAdmin(admin.ModelAdmin):
    list_display = ("kode_skpd", "nama_skpd", "id_lokasi_bidang")
    ordering = ["id"]
    list_per_page = 10



class StatusPegawaiAdmin(admin.ModelAdmin):
    list_display = ("status_pegawai",)
    ordering = ["id"]
    list_per_page = 10



class PegawaiAdmin(admin.ModelAdmin):
    list_display = ("nama_pegawai", "nip", "pangkat", "id_status_pegawai", "id_skpd")
    ordering = ["id"]
    list_per_page = 10



class SPPDAdmin(admin.ModelAdmin):
    list_display = ("no_sppd", "id_skpd", "id_pegawai", "tanggal_berangkat",
                    "tanggal_kembali", "dibayar", "keterangan", )
    ordering = ["no_sppd"]
    form = DibayarForm
    save_as = True
    date_hierarchy = 'tanggal_berangkat'
    search_fields = ['no_sppd']
    list_per_page = 10




#REGISTER ADMIN
admin.site.register(Provinsi, ProvinsiAdmin)
admin.site.register(Kabupaten, KabupatenAdmin)
admin.site.register(LokasiBidang, LokasiBidangAdmin)
admin.site.register(SKPD, SKPDAdmin)
admin.site.register(StatusPegawai, StatusPegawaiAdmin)
admin.site.register(Pegawai, PegawaiAdmin)
admin.site.register(SPPD, SPPDAdmin)
