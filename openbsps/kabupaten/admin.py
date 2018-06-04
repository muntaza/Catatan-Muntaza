# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from kabupaten.models import Provinsi, Kabupaten, Kecamatan, Desa
from kabupaten.models import Status, RT, JenisKelamin, Penduduk
from kabupaten.models import Tahun, Penerima, PendudukPenerima

from kabupaten.forms import BantuanForm

class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ("nama_provinsi",)

class KabupatenAdmin(admin.ModelAdmin):
    list_display = ("nama_kabupaten", "id_provinsi",)

class KecamatanAdmin(admin.ModelAdmin):
    list_display = ("nama_kecamatan", "id_kabupaten",)

class DesaAdmin(admin.ModelAdmin):
    list_display = ("nama_desa", "id_kecamatan",)

class StatusAdmin(admin.ModelAdmin):
    list_display = ("status",)

class RTAdmin(admin.ModelAdmin):
    list_display = ("rt",)

class JenisKelaminAdmin(admin.ModelAdmin):
    list_display = ("kode_jenis_kelamin", "jenis_kelamin",)


class PendudukAdmin(admin.ModelAdmin):
    list_display = ("no_ktp", "nama", "id_desa",)
    ordering = ["no_ktp",]
    search_fields = ["nama", "no_ktp",]
    list_filter = ["id_desa",]
    form = BantuanForm

    def get_queryset(self, request):
        return self.model.objects.filter(id_status__in=[1,2,])

class TahunAdmin(admin.ModelAdmin):
    list_display = ("tahun",)

class PenerimaInline(admin.TabularInline):
    model = Penerima
    extra = 0

class PendudukPenerimaAdmin(admin.ModelAdmin):
    inlines = [PenerimaInline, ]
    list_display = ("no_ktp", "nama", "id_desa",)
    ordering = ["no_ktp",]
    search_fields = ["nama", "no_ktp",]
    list_filter = ["id_desa",]
    form = BantuanForm
#   readonly_fields = ["no_ktp", ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_status":
            kwargs["queryset"] = Status.objects.filter(id__in=[2,3,])
        return super(PendudukPenerimaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_status__exact=3)



#Register Admin
admin.site.register(Provinsi, ProvinsiAdmin)
admin.site.register(Kabupaten, KabupatenAdmin)
admin.site.register(Kecamatan, KecamatanAdmin)
admin.site.register(Desa, DesaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(RT, RTAdmin)
admin.site.register(JenisKelamin, JenisKelaminAdmin)
admin.site.register(Penduduk, PendudukAdmin)
admin.site.register(Tahun, TahunAdmin)
admin.site.register(PendudukPenerima, PendudukPenerimaAdmin)
