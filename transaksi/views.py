from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from barang.forms import BarangForms
from django.contrib.auth.decorators import login_required
from transaksi.forms import *
from transaksi.models import *
from barang.models import *

@login_required(login_url='/accounts/')
def transaksi(request):
    transaksi = TransaksiPembelianForm()
    if request.method == 'POST':
        transaksi = TransaksiPembelianForm(request.POST)
        if transaksi.is_valid():
            transaksi.save()
            return redirect('/')
        else:
            return HttpResponse("SomethingWrong")  
    else:
        return render(request, 'transaksi.html', {'form':transaksi})
    # form_barang1 = TransaksiPembelian.objects.all()
    # barang1 = []
    # for u in form_barang1:
    #     barang1.append(u)
    #     print(u)
    # if request.method == 'POST':
    #     # barang = TransaksiPembelianForm(request.POST)
    #     if barang1.is_valid():
    #         barang1.save()
    #         return redirect('/')
    #     else:
    #         return HttpResponse("SomethingWrong")  
    # else:
            
    #     return render(request, 'transaksi.html', {'form':form_barang, 'data':barang1})
        

        # if request.method == "POST":
        #     if get_code:
        #         save_product = TblBarang()
        #         save_product = get_code
        #         save_product.save()
        #         messages.success(request, "Selamat Anda Berhasil")
        #         return redirect('transaksi.html')
        #     else:
        #         return HttpResponse("SomethingWrong")  
        # else:
        #     return render(request, 'transaksi.html', {'data':product,'nama_barang':u.nama_barang})
            
    # form_transaksi = TransaksiPembelian.objects.all()
    # return render(request, 'transaksi.html', {'data':form_transaksi})
# def create_transaksi(request):
#     form_transaksi = TransaksiPembelianForm()
#     if request.method == 'POST':
#         transaksi = TransaksiPembelianForm(request.POST)
#         if transaksi.is_valid():
#             transaksi.save()
#             return redirect('/')
#         else:
#             return HttpResponse("SomethingWrong")  
#     else:
#         return render(request, 'transaksi.html', {'form':form_transaksi})\
@login_required(login_url='/accounts/')
def detail_transaksi(req, id):
    detail_transaksi = TransaksiPembelian.objects.get(id=id)
    data = TransaksiPembelianForm(detail_transaksi, many=False)
    data1 = data.data    
    return render(req, 'transaksi_detail.html', {
        'data': data1,
    })

@login_required(login_url='/accounts/')
def delete_transaksi(req, id):
    TransaksiPembelian.objects.get(id=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/')

@login_required(login_url='/accounts/')
def update_transaksi(req, id):
    if req.POST:
        data = TransaksiPembelian.objects.filter(pk=id).update(
            name=req.POST['name'], 
            phone=req.POST['phone'], 
            address=req.POST['address'], 
            date=req.POST['date'])
        return redirect('/transaksi/')

    data = TransaksiPembelian.objects.filter(pk=id).first()    
    return render(req, 'transaksi_update.html', {
        'data': data,
    })