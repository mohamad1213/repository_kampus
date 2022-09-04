from django.http import HttpResponse
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
import requests
def index(request):
    response = requests.get("https://zenquotes.io/api/quotes/")
    if response.status_code == 200:
        ## extracting the core data
        json_data = response.json()
        data = json_data[1]['q']
    else:
        print("Error while getting quote")
    return render(request, 'home.html',{'data':data})

def detail(request, pk):
    post = UploadSkripsi.objects.filter(id=pk)
    post1 = Upload.objects.filter(id=pk)
    if post:
        fav = False
        for u in post:
            if u.favourite.filter(id=request.user.id).exists():
                fav = True
        return render(request, 'details.html', {'skripsi':post, 'is_favourite':fav})
    elif post1:
        fav = False
        for u in post1:
            if u.favourite.filter(id=request.user.id).exists():
                fav = True
        return render(request, 'details_katul.html', {'skripsi':post1, 'is_favourite':fav})

# @login_required(login_url='/accounts/')
def home(request):
    group = request.user.groups.first()
    if group is not None and group.name == 'admin':
        data = Upload.objects.all()
        if request.method == "POST":  
            form = UploadForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save() 
                    model = form.instance
                    messages.success(request, 'You did it')
                    return redirect('administration:admin')  
                except:  
                    pass  
        else:  
            form = UploadForm()
        return render(request, '/administration/index.html', {
            'data':data,
            'form':form,
        })
    elif group is not None and group.name == 'user':
        group = request.user.groups.first()
        data = Upload.objects.all()
        if request.method == "POST":  
            form = UploadForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save() 
                    model = form.instance
                    messages.success(request, 'You did it')
                    return redirect('/')  
                except:  
                    pass  
        else:  
            form = UploadForm()
        return render(request, 'home.html', {
            'data':data,
            'form':form
        })
    else:
        data = Upload.objects.all()
        if request.method == "POST":  
            form = UploadForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save() 
                    model = form.instance
                    messages.success(request, 'You did it')
                    return redirect('index')  
                except:  
                    pass  
        else:  
            form = UploadForm()
        return render(request, 'home.html', {
            'data':data,
            'form':form
        })

@login_required(login_url='/accounts/')
def user(request):
    data = Upload.objects.all()
    response = request.get("https://zenquotes.io/api/quotes/")
    if response.status_code == 200:
        ## extracting the core data
        json_data = response.json()
        # data = json_data['q']
        print(json_data[1]['q'])
    else:
        print("Error while getting quote")
    return render(request, 'home.html',{'data':data})

# @login_required(login_url='/accounts/')
def simpan(request,pk):
    video = get_object_or_404(Upload, id=pk)
    if request.method == 'POST':
        video.favourite.add(request.user)

    return redirect('/user_view/%s' % pk)


    
@login_required(login_url='/accounts/')
def admin(request):
    return render(request, 'admin/admin.html')

@login_required(login_url='/accounts/')
def user_view(request):
    data = Upload.objects.all()
    return render(request, 'user_view/user_view.html', {
        'data':data
    })
    
@login_required(login_url='/accounts/')
def detail_view(request, id):
    data = Upload.objects.filter(pk=id)
    for u in data:
        upload = f'media/{u.upload}'
        print(upload)
    return render(request, 'user_view/detail_view.html', {
        'data': data,
        'upload':upload
    })
@login_required(login_url='/accounts/')
def user_detail(request, id):
    data = Upload.objects.filter(pk=id)
    for u in data:
        upload = f'media/{u.upload}'
    return render(request, 'user/detail_view.html', {
        'data': data,
        'upload':upload

    })

def artists_view(request):
    if 'q' in request.GET:
        query = request.GET['q']
        multiple_q = Q(judul_laporan__icontains=query) | Q(jenis_laporan__icontains=query) | Q(abstrak__icontains=query) | Q(nama_penulis__icontains=query) | Q(prodi__icontains=query) | Q(tahun_penyelesaian__icontains=query) | Q(nim_siswa__icontains=query)
        multiple_q2 = Q(judul_laporan__icontains=query) | Q(abstrak__icontains=query) | Q(nama_penulis__icontains=query) | Q(prodi__icontains=query) | Q(tahun_penyelesaian__icontains=query) | Q(nim_siswa__icontains=query)
        results1 = Upload.objects.filter(multiple_q)
        results2 = UploadSkripsi.objects.filter(multiple_q2)
        results = chain(results1, results2)
    else:
        results3 = UploadSkripsi.objects.all()
        results4 = Upload.objects.all()
        results = chain(results3, results4)
    context ={
        'results': results
    }
    return render(request, 'page_result.html', context)

def post_favorite(request, pk):
    post1 = get_object_or_404(UploadSkripsi,id=pk)
    if post1.favourite.filter(pk=request.user.id).exists():
        post1.favourite.remove(request.user)
    else:
        post1.favourite.add(request.user)
    return HttpResponseRedirect('/list_fav/')
# def post_favorite(request, pk):
#     post1 = get_object_or_404(UploadSkripsi,id=pk)
#     post2= get_object_or_404(Upload,id=pk)
#     if post1.favourite.filter(pk=request.user.id).exists() and post2.favourite.filter(pk=request.user.id).exists():
#         post1.favourite.remove(request.user)
#         post2.favourite.remove(request.user)
#     else:
#         post1.favourite.add(request.user)
#         post2.favourite.add(request.user)
#     return HttpResponseRedirect('/list_fav/')
def list_fav(request):
    user = request.user
    fav_post = user.fav3.all()
    context = {
        'fav_post':fav_post
    }
    return render(request, 'bookmark.html', context)
def remove(request,pk):
     product = get_object_or_404(Contoh,pk=pk)
     if request.user in product.favourite.all():
         product.favourite.remove(request.user)
     return HttpResponseRedirect('/')