# Generated by Django 4.0.5 on 2022-08-09 16:10

import admin1.validator
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadSkripsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodi', models.CharField(choices=[('Informatika', 'Informatika'), ('Teknik Komputer', 'Teknik Komputer'), ('Teknik Elektro', 'Teknik Elektro')], max_length=50)),
                ('judul_laporan', models.CharField(max_length=100)),
                ('tahun_penyelesaian', models.IntegerField()),
                ('nama_penulis', models.CharField(max_length=50)),
                ('nim_siswa', models.IntegerField()),
                ('lampiran', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('cover', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('abstrak', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('daftarisi', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('bab1', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('bab2', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('bab3', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('bab4', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('bab5', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('dapus', models.FileField(blank=True, default='', upload_to='skripsi/', validators=[admin1.validator.validate_file_extension])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='skripsi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_laporan', models.CharField(choices=[('Jurnal', 'Jurnal'), ('Project', 'Project'), ('Thesis', 'Thesis')], default='', max_length=50)),
                ('prodi', models.CharField(choices=[('Informatika', 'Informatika'), ('Teknik Komputer', 'Teknik Komputer'), ('Teknik Elektro', 'Teknik Elektro')], max_length=50)),
                ('judul_laporan', models.CharField(max_length=100)),
                ('tahun_penyelesaian', models.IntegerField()),
                ('abstrak', models.TextField(max_length=500)),
                ('nama_penulis', models.CharField(max_length=50)),
                ('nim_siswa', models.IntegerField()),
                ('upload', models.FileField(blank=True, default='', upload_to='karyatulis/', validators=[admin1.validator.validate_file_extension])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='karyatulis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('alamat', models.TextField(null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
