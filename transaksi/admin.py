from django.contrib import admin
from .models import *

class TblBarangAdmin(admin.ModelAdmin):
    list_display = [ 'code_brg']
admin.site.register(TblBarang, TblBarangAdmin)

class TransaksiPembelianAdmin(admin.ModelAdmin):
    list_display = ['id_transaksi', 'code_brg']
admin.site.register(TransaksiPembelian, TransaksiPembelianAdmin)
