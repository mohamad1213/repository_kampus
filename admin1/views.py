from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import ProfileUser
import os
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

######################################## DASHBOARD #####################################

@login_required(login_url='/accounts/')
def index(request):
    skripsi = UploadSkripsi.objects.filter(owner=request.user)
    karlis = Upload.objects.filter(owner=request.user)
    profile = ProfileUser.objects.all()
    context ={'data':len(skripsi),'karlis':len(karlis), 'user':len(profile)}
    return render(request,"index.html", context)

######################################## SKRIPSI #####################################
@login_required(login_url='/accounts/')
def ListMhs(request):
    profile = ProfileUser.objects.all()
    return render(request, 'mhs/index.html',{
        'profile': profile,
        
    })
@login_required(login_url='/accounts/')
def DetailMhs(req, pk):
    data = ProfileUser.objects.filter(id=pk).first()
    return render(req, 'mhs/detail.html', {"data":data})
@login_required(login_url='/accounts/')
def ListJournal(request):
    tasks = Upload.objects.filter(owner=request.user)
    form_input = UploadForm()
    if request.POST:
        form_input = UploadForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/journal/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'journal/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })

@login_required(login_url='/accounts/')
def CreateJournal(request):
    form_input = UploadForm()
    if request.POST:
        form_input = UploadForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/journal/')
        else:
            print(form_input.errors)
    else:
        form_input = UploadForm()
    context ={
        'form':form_input
    }
    return render(request, 'journal/create.html', context)
@login_required(login_url='/accounts/')
def UpdateJournal(request, pk):
    instance =get_object_or_404(Upload,id=pk)
    form_journal = UploadForm(instance=instance)
    if request.POST:
        form_journal = UploadForm(request.POST, request.FILES,instance=instance)
        if form_journal.is_valid():
            form_journal.owner = request.user
            form_journal.save()
            messages.success(request, "Data Telah diupdate")
            return redirect('/administration/journal/')
    context = {"data":form_journal}
    return render(request, 'journal/update.html', context) 

@login_required(login_url='/accounts/')
def DeleteJournal(req, pk):
    Upload.objects.get(id=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/journal/')

@login_required(login_url='/accounts/')
def DetailJournal(req, pk):
    data = Upload.objects.filter(id=pk).first()
    return render(req, 'journal/detail.html', {"data":data})

######################################## SKRIPSI #####################################
@login_required(login_url='/accounts/')
def ListSkripsi(request):
    tasks = UploadSkripsi.objects.filter(owner=request.user)
    return render(request, 'skripsi/index.html',{
        'data': tasks,
        
    })
def CreateSkrispi(request):
    form_input = UploadSkripsiForm()
    if request.POST:
        form_input = UploadSkripsiForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/skripsi/')
    else:
        form_input = UploadSkripsiForm()
    context ={
        'form':form_input
    }
    return render(request, 'skripsi/create.html', context)
@login_required(login_url='/accounts/')
def UpdateSkripsi(request, pk):
    instance =get_object_or_404(UploadSkripsi,id=pk)
    form_skripsi = UploadSkripsiForm(instance=instance)
    if request.POST:
        form_skripsi = UploadSkripsiForm(request.POST, request.FILES,instance=instance)
        if form_skripsi.is_valid():
            form_skripsi.owner = request.user
            form_skripsi.save()
            messages.success(request, "Data Telah diupdate")
            return redirect('/administration/skripsi/')
    context = {"data":form_skripsi} 
    return render(request, 'skripsi/update.html', context) 
    
@login_required(login_url='/accounts/')
def DeleteSkrispi(req, pk):
    UploadSkripsi.objects.get(id=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/skripsi/')

@login_required(login_url='/accounts/')
def DetailSkripsi(req, pk):
    data = UploadSkripsi.objects.filter(id=pk).first()
    return render(req, 'skripsi/detail.html', {"data":data})

@login_required(login_url='/accounts/')
def AccountsSettings(request):
    user = Profile.objects.filter(user=request.user).first()
    user2 = User.objects.filter(email=request.user.email).first()
    form = ProfileForm(instance=user)
    form2 = ProfileForm2(instance=user2)
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)
        form2 = ProfileForm2(request.POST, request.FILES, instance=user2)
        if form.is_valid() and form2.is_valid():
            form.instance.user = request.user
            form2.email = form2.cleaned_data['email']
            form.save()
            form2.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/profile/')
        else:
            print(form.errors)
            print(form2.errors)
    else:
        form = ProfileForm(instance=user)
        form2 = ProfileForm2(instance=user2)
    context ={
        'form_admin':form,
        'form_admin2':form2,
    }
    return render(request, 'profile/profile.html', context)

