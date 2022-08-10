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
def index(request):
    home = Home.objects.all()
    berita =Berita.objects.all()
    tentang = TentangKami.objects.all()
    galeri = Galeri.objects.all()
    prestasi = Prestasi.objects.all()
    ppdb = Pendaftaran.objects.all()
    visi = Visimisi.objects.all()
    ukm = Ekstrakulikuler.objects.all()
    context = {
        'home':home,
        'berita':berita,
        'tentang':tentang,
        'visi':visi,
        'galeri':galeri,
        'prestasi':prestasi,
        'ppdb':ppdb,
        'ukm':ukm,
    }
    return render(request,"home.html", context)
def page(request):
    home = Home.objects.all()
    berita =Berita.objects.all()
    tentang = TentangKami.objects.all()
    galeri = Galeri.objects.all()
    prestasi = Prestasi.objects.all()
    ppdb = Pendaftaran.objects.all()
    visi = Visimisi.objects.all()
    ukm = Ekstrakulikuler.objects.all()
    context = {
        'home':home,
        'berita':berita,
        'tentang':tentang,
        'visi':visi,
        'galeri':galeri,
        'prestasi':prestasi,
        'ppdb':ppdb,
        'ukm':ukm,
    }
    return render(request,"page_result.html", context)
def detail(request):
    home = Home.objects.all()
    berita =Berita.objects.all()
    tentang = TentangKami.objects.all()
    galeri = Galeri.objects.all()
    prestasi = Prestasi.objects.all()
    ppdb = Pendaftaran.objects.all()
    visi = Visimisi.objects.all()
    ukm = Ekstrakulikuler.objects.all()
    context = {
        'home':home,
        'berita':berita,
        'tentang':tentang,
        'visi':visi,
        'galeri':galeri,
        'prestasi':prestasi,
        'ppdb':ppdb,
        'ukm':ukm,
    }
    return render(request,"details.html", context)


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
        return render(request, 'user/home.html', {
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
    response = requests.get("https://zenquotes.io/api/quotes/")
    if response.status_code == 200:
        ## extracting the core data
        json_data = response.json()
        # data = json_data['q']
        print(json_data[1]['q'])
    else:
        print("Error while getting quote")
    # search = 'Jasper Fforde'
    # hasil =[]
    # result = quote(search, limit=2)
    # for u in result:
    #     hasil.append(u['qoute'])
    # print(hasil)
    return render(request, 'user/user.html',{'data':data})

# @login_required(login_url='/accounts/')
def simpan(request,pk):
    video = get_object_or_404(Upload, id=pk)
    if request.method == 'POST':
        video.favourite.add(request.user)

    return redirect('/user_view/%s' % pk)

def remove(request,pk):
     product = get_object_or_404(Upload,pk=pk)
     if request.user in product.favourite.all():
         product.favourite.remove(request.user)
     return HttpResponseRedirect('/')

    
# @login_required(login_url='/accounts/')
# def simpan(request, id):
#     upload = Upload.objects.get(pk=id)
#     data = {
#             "id": upload.id,
#             "prodi": upload.prodi,
#             "jenis_laporan": upload.jenis_laporan,
#             "judul_laporan": upload.judul_laporan,
#             "tahun_penyelesaian": upload.tahun_penyelesaian,
#             "abstrak": upload.abstrak,
#             "nama_penulis": upload.nama_penulis,
#             "upload": upload.upload,
#     }
#     if request.method == "POST":
#         upload_forms = UploadForm(request.POST, instance=data)
#         if upload_forms.is_valid():
#             print('save')
#             upload_forms.save()
#             print('save')
#             return redirect('user')
#         else:
#             return HttpResponse("salah cok")
        
#     return render(request, 'user.html', {'data': data, 'form':upload_forms})
    

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
        results = Upload.objects.filter(multiple_q)
        results = UploadSkripsi.objects.filter(multiple_q)
    else:
        results = Upload.objects.all()
        results = UploadSkripsi.objects.all()
    return render(request, 'page_result.html', {'results': results})
