# Generated by Django 4.0.5 on 2022-10-12 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='jenis_laporan',
        ),
    ]
