from django.db import models
from barang.models import TblBarang
import datetime
import pytz
tz = pytz.timezone("Asia/Jakarta")

class TransaksiPembelian(models.Model):
    TypeTransaksi = [
        ('Jual', 'Jual'),
        ('Beli', 'Beli'),
    ]
    Tipetransaksi = models.CharField(
        max_length=4,
        choices=TypeTransaksi,
    )
    id_transaksi = models.AutoField(primary_key=True)
    no_faktur = models.CharField(unique=True,auto_created=True,max_length=200)
    code_brg = models.ForeignKey(TblBarang, on_delete=models.DO_NOTHING)
    qty = models.FloatField()
    jumlah_uang = models.FloatField()
    total_belanja = models.FloatField()
    uang_kembali = models.FloatField()
    tgl = models.DateField(default=datetime.datetime.now().astimezone(tz).strftime("%d-%m-%Y"))

    @property
    def tanggal_format(self):
        return self.tgl.strftime('%Y-%m-%d')

    def harga(self):
        return self.code_brg.harga_barang
    
    def nama_barang(self):
        return self.code_brg.nama_barang

    def jumlah_uang1(self):
        return self.harga * self.qty

class TransaksiPenjualan(models.Model):
    id_transaksi = models.AutoField(primary_key=True)
    no_faktur = models.CharField(max_length=200)
    kd_barang = models.CharField(max_length=15)
    jumlah_uang = models.FloatField()
    total_belanja = models.FloatField()
    uang_kembali = models.FloatField()