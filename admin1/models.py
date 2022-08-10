from django.db import models
from .validator import validate_file_extension

from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	alamat = models.TextField(null=True)
	profile_pic = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Upload(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='karyatulis')
    PRODI_CHOICE = (
        ('Informatika', 'Informatika'),
        ('Teknik Komputer', 'Teknik Komputer'),
        ('Teknik Elektro', 'Teknik Elektro'),
    )
    LAPORAN_CHOICES = (
        ('Jurnal','Jurnal'),
        ('Project','Project'),
        ('Thesis','Thesis'),
    )
    jenis_laporan = models.CharField(default='',max_length=50,choices=LAPORAN_CHOICES)
    prodi = models.CharField(max_length=50, choices=PRODI_CHOICE)
    judul_laporan = models.CharField(max_length=100)
    tahun_penyelesaian = models.IntegerField()
    abstrak= models.TextField(max_length=500)
    nama_penulis=models.CharField(max_length=50)
    nim_siswa=models.IntegerField()
    upload = models.FileField(default='', upload_to='karyatulis/', null=False, blank=True,validators=[validate_file_extension])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # favourite = models.ManyToManyField(UploadRepo, related_name="fav", blank=True)
from django.db import models

class UploadSkripsi(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='skripsi')
    PRODI_CHOICE = (
        ('Informatika', 'Informatika'),
        ('Teknik Komputer', 'Teknik Komputer'),
        ('Teknik Elektro', 'Teknik Elektro'),
    )
    prodi = models.CharField(max_length=50, choices=PRODI_CHOICE)
    judul_laporan = models.CharField(max_length=100)
    tahun_penyelesaian = models.IntegerField()
    abstrak= models.TextField()
    nama_penulis=models.CharField(max_length=50)
    nim_siswa=models.IntegerField()
    lampiran = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    cover = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    daftarisi = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    bab1 = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    bab2 = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    bab3 = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    bab4 = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    bab5 = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    dapus = models.FileField(default='', upload_to='skripsi/', null=False, blank=True,validators=[validate_file_extension])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)