from aiohttp import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

@login_required(login_url='/accounts/')
def index(request):
    skripsi = UploadSkripsi.objects.filter(owner=request.user)
    karlis = Upload.objects.filter(owner=request.user)
    context ={'data':len(skripsi),'karlis':len(karlis)}
    return render(request,"index.html", context)
#karya_tulis 
@login_required(login_url='/accounts/')
def karya_tulis(request):
    tasks = Upload.objects.filter(owner=request.user)
    form_input = UploadForm()
    if request.POST:
        form_input = UploadForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/karya_tulis/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'karya_tulis/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_karya_tulis(req, pk):
    instance = Upload.objects.get(id=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.upload) > 0:
                os.remove(instance.upload.path)
            instance.upload = req.FILES['upload']
        instance.prodi = req.POST.get('prodi')
        instance.judul_laporan = req.POST.get('judul_laporan')
        instance.tahun_penyelesaian = req.POST.get('tahun_penyelesaian')
        instance.abstrak = req.POST.get('abstrak')
        instance.nim = req.POST.get('nim')
        instance.nama_penulis = req.POST.get('nama_penulis')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/karya_tulis/')
    context = {"data":instance}
    return render(req, 'karya_tulis/update.html', context) 

@login_required(login_url='/accounts/')
def delete_karya_tulis(req, pk):
    Upload.objects.get(id=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/karya_tulis/')

@login_required(login_url='/accounts/')
def detail_karya_tulis(req, pk):
    data = Upload.objects.filter(id=pk).first()
    return render(req, 'karya_tulis/detail.html', {"data":data})

##Berita
@login_required(login_url='/accounts/')
def skripsi(request):
    tasks = UploadSkripsi.objects.filter(owner=request.user)
    form_input = UploadSkripsiForm()
    if request.POST:
        form_input = UploadSkripsiForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/skripsi/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'skripsi/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_skripsi(req, pk):
    instance = UploadSkripsi.objects.get(id=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.bab1) > 0:
                os.remove(instance.bab1.path)
            instance.bab1 = req.FILES['bab1']
            if len(instance.bab2) > 0:
                os.remove(instance.bab2.path)
            instance.bab2 = req.FILES['bab2']
            if len(instance.bab3) > 0:
                os.remove(instance.bab3.path)
            instance.bab3 = req.FILES['bab3']
            if len(instance.bab4) > 0:
                os.remove(instance.bab4.path)
            instance.bab4 = req.FILES['bab4']
            if len(instance.bab5) > 0:
                os.remove(instance.bab5.path)
            instance.bab5 = req.FILES['bab5']
            if len(instance.bab5) > 0:
                os.remove(instance.bab5.path)
            instance.bab5 = req.FILES['bab5']
            if len(instance.lampiran) > 0:
                os.remove(instance.lampiran.path)
            instance.lampiran = req.FILES['lampiran']
            if len(instance.dapus) > 0:
                os.remove(instance.dapus.path)
            instance.dapus = req.FILES['dapus']
            if len(instance.daftarisi) > 0:
                os.remove(instance.daftarisi.path)
            instance.daftarisi = req.FILES['daftarisi']
            if len(instance.abstrak) > 0:
                os.remove(instance.abstrak.path)
            instance.abstrak = req.FILES['abstrak']
        instance.prodi = req.POST.get('prodi')
        instance.judul_laporan = req.POST.get('judul_laporan')
        instance.tahun_penyelesaian = req.POST.get('tahun_penyelesaian')
        instance.abstrak = req.POST.get('abstrak')
        instance.nim = req.POST.get('nim')
        instance.nama_penulis = req.POST.get('nama_penulis')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/skripsi/')
    context = {"data":instance} 
    return render(req, 'skripsi/update.html', context) 
    
@login_required(login_url='/accounts/')
def delete_skripsi(req, pk):
    UploadSkripsi.objects.get(id=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/skripsi/')

@login_required(login_url='/accounts/')
def detail_skripsi(req, pk):
    data = UploadSkripsi.objects.filter(id=pk).first()
    return render(req, 'skripsi/detail.html', {"data":data})

@login_required(login_url='/accounts/')
def accountSettings(req, pk):
    instance = Profile.objects.get(id=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.profile_pic) > 0:
                os.remove(instance.profile_pic.path)
            instance.profile_pic = req.FILES['profile_pic']
        instance.name = req.POST.get('name')
        instance.phone = req.POST.get('phone')
        instance.email = req.POST.get('email')
        instance.alamat = req.POST.get('alamat')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/profile/')
    context = {"data":instance}
    return render(req, 'profile/update.html', context)

@login_required(login_url='/accounts/')
def profile(req):
    data = Profile.objects.all()
    return render(req, 'profile/index.html', {'data': data})


