from http.client import HTTPResponse
from admin1.models import *
from admin1.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.http import HttpResponseRedirect, HttpResponse
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



def artists_view(request):
    if 'q' in request.GET:
        query = request.GET['q']
        multiple_q = Q(judul_laporan__icontains=query) | Q(abstrak__icontains=query) | Q(nama_penulis__icontains=query) | Q(prodi__icontains=query) | Q(tahun_penyelesaian__icontains=query) | Q(nim_siswa__icontains=query)
        journal = Upload.objects.filter(multiple_q)
        skripsi = UploadSkripsi.objects.filter(multiple_q)
    else:
        journal = Upload.objects.all()
        skripsi = UploadSkripsi.objects.all()
    context ={
        'journal':journal,
        'skripsi':skripsi,
    }
    return render(request, 'page_result.html', context)


def post_favorite(request, pk):
    post1 = get_object_or_404(UploadSkripsi,id=pk)
    if post1.favourite.filter(pk=request.user.id).exists():
        post1.favourite.remove(request.user)
        messages.success(request,'Data telah dihapus')
    else:
        post1.favourite.add(request.user)
        messages.success(request,'Data telah ditambahkan')
    return HttpResponseRedirect('/list_fav/')

    
def post_favorite_kartul(request, pk):
    post2 = get_object_or_404(Upload,id=pk)
    if post2.favourite.filter(pk=request.user.id).exists():
        post2.favourite.remove(request.user)
        messages.success(request, 'bookmark telah dihapus')
    else:
        post2.favourite.add(request.user)
        messages.success(request, 'bookmark telah ditambahkan')
    return HttpResponseRedirect('/list_fav/')

@login_required(login_url='/accounts/')
def list_fav(request):
    user = request.user
    kartul = user.fav.all()
    skripsi = user.fav2.all()
    notfound = 'Data not Found'
    if kartul :
        kartul = user.fav.all()
        skripsi = user.fav2.all()
        context = {
        'journal':kartul,
        'skripsi':skripsi,
        }
        return render(request, 'bookmark.html', context)
    elif skripsi :
        skripsi = user.fav2.all()
        kartul = user.fav.all()
        context = {
        'journal':kartul,
        'skripsi':skripsi,
        }
        return render(request, 'bookmark.html', context)
    else:
        notfound = 'Data not Found'
    context = {
        'journal':kartul,
        'skripsi':skripsi,
        'notfound':notfound,
    }
    return render(request, 'bookmark.html', context)



@login_required(login_url='/accounts/')
def AccountsSettings(request):
    user = ProfileUser.objects.filter(user=request.user).first()
    print(user)
    form = ProfileUserForm(instance=user)
    if request.POST:
        form = ProfileUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/profile/')
        else:
            print(form.errors)
    else:
        form = ProfileUserForm(instance=user)
    context ={
        'form':form,
    }
    return render(request, 'profile/index.html', context)

