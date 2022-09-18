from admin1.models import *
from admin1.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from itertools import chain

from home.forms import ProfileUserForm
def home(request):
    group = request.user.groups.first()
    if group is not None and group.name == 'admin':
        messages.success(request, 'Selamat Datang Admin')
        return HttpResponseRedirect('/administration/')
    elif group is not None and group.name == 'user':
        group = request.user.groups.first()
        return render(request, 'home.html', {
            # 'data':data,
        })
    else:
        return render(request, 'home.html', {
            # 'data':data,
        })
def detail(request, pk):
    post = UploadSkripsi.objects.filter(id=pk)
    post1 = Upload.objects.filter(id=pk)
    context = {
        'kartul':post1,
        'skripsi':post,
    }
    return render(request, 'details.html' ,context)

@login_required(login_url='/accounts/')
def user_detail(request, id):
    data = Upload.objects.filter(pk=id)


def artists_view(request):
    if 'q' in request.GET:
        query = request.GET['q']
        multiple_q = Q(judul_laporan__icontains=query) | Q(jenis_laporan__icontains=query) | Q(abstrak__icontains=query) | Q(nama_penulis__icontains=query) | Q(prodi__icontains=query) | Q(tahun_penyelesaian__icontains=query) | Q(nim_siswa__icontains=query)
        multiple_q2 = Q(judul_laporan__icontains=query) | Q(abstrak__icontains=query) | Q(nama_penulis__icontains=query) | Q(prodi__icontains=query) | Q(tahun_penyelesaian__icontains=query) | Q(nim_siswa__icontains=query)
        results1 = Upload.objects.filter(multiple_q)
        results2 = UploadSkripsi.objects.filter(multiple_q2)
        results = chain(results1, results2)
    else:
        results1 = Upload.objects.all()
        results2 = UploadSkripsi.objects.all()
        results = chain(results1, results2)
    context ={
        'kartul':results2,
        'skripsi':results1,
        'results': results
    }
    return render(request, 'page_result.html', context)

def post_favorite(request, pk):
    post1 = get_object_or_404(UploadSkripsi,id=pk)
    if post1.favourite.filter(pk=request.user.id).exists():
        post1.favourite.remove(request.user)
        messages.error(request,'Data telah dihapus')

    else:
        post1.favourite.add(request.user)
        messages.success(request,'Data telah ditambahkan')
    return HttpResponseRedirect('/results/')

def post_favorite_kartul(request, pk):
    post1 = get_object_or_404(Upload,id=pk)
    if post1.favourite.filter(pk=request.user.id).exists():
        post1.favourite.remove(request.user)
    else:
        post1.favourite.add(request.user)
    return HttpResponseRedirect('/results/')

@login_required(login_url='/accounts/')
def list_fav(request):
    user = request.user
    kartul = user.fav.all()
    skripsi = user.fav2.all()
    fav_post = chain(kartul, skripsi)
    context = {
        'fav_post':fav_post,
    }
    return render(request, 'bookmark.html', context)
# def remove(request,pk):
#      product = get_object_or_404(Contoh,pk=pk)
#      if request.user in product.favourite.all():
#          product.favourite.remove(request.user)
#      return HttpResponseRedirect('/')


@login_required(login_url='/accounts/')
def AccountsSettings(request):
    user = request.user.profileuser
    form = ProfileUserForm(instance=user)
    if request.POST:
        form = ProfileUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/profile/')
    else:
        form = ProfileUserForm(instance=user)
    context ={
        'form':form,
    }
    return render(request, 'profile/index.html', context)

