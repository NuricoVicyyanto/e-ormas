from collections import Counter
from datetime import timedelta
from django.db.models import Count
from itertools import count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os
from eormasapp.forms import *
from eormasapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import csv

def file_load_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nama Ormas', 'Jenis Ormas','Bidang Ormas', 'Alamat', 'Kelurahan', 'Kecamatan', 'Kabupaten','Nama Notaris', 'Nomor Notaris', 'Nama Ketua', 
    'ttl Ketua', 'Nomor Ketua', 'Nama Sekretaris','ttl Sekretaris','Nomor Sekretaris', 'Nama Bendahara','ttl Bendahara', 'noBendahara'])

    ormas = Ormas.objects.filter(status= '1')

    # Note: we convert the students query set to a values_list as the writerow expects a list/tuple       
    ormas = ormas.all().values_list('nama', 'unsur','bidang', 'alamat', 'desa', 'kecamatan', 'kabupaten','namaNotaris', 'noNotaris', 'namaKetua', 
    'ttlKetua', 'noKetua', 'namaSekretaris','ttlSekretaris','noSekretaris', 'namaBendahara','ttlBendahara', 'noBendahara')

    for ormas in ormas:
        writer.writerow(ormas)

    return response



# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # ormas = Ormas.objects.all()
            if request.user.is_superuser:
                return redirect('data_ormas')
            else:
                return redirect('pendaftaran')
        else:
            messages.info(request, 'Username or password is incorrect')

    konteks = {}
    return render(request, 'backend/login.html', konteks)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return  redirect('dashboard')

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('username')
            # group = Group.objects.get(name='ormas')
            # user.groups.add(group)
            # Ormas.objects.create(
			# 	user=user,
			# 	)
            messages.success(request, 'Account was created')
            return redirect('login')

    konteks = {'form': form}
    return render(request, 'backend/register.html', konteks)


@login_required(login_url='login')
def index(request):
    return render(request, 'backend/index.html')

@login_required(login_url='login')
def landing(request):
    return render(request, 'backend/landing.html')

def dashboard(request):
    informasi = Informasi.objects.all()

    konteks ={
        'informasi':informasi,
    }

    return render(request, 'frontend/home.html', konteks)



def ormas(request):
    ormas = Ormas.objects.filter(status= '1')

    konteks ={
        'ormas':ormas,
    }

    return render(request, 'frontend/ormas.html', konteks)


def ormasUnsur(request):
    ormas = Ormas.objects.values('unsur').filter(status = '1').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')

    konteks ={
            'ormas':ormas,
        }
    return render(request, 'frontend/ormas_uns.html', konteks)

def ormasDesa(request):
    ormas = Ormas.objects.values('desa').filter(status = '1').annotate(
        jumlah=Count('desa')
    ).order_by('desa')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'frontend/ormas_ds.html', konteks)


def ormasKecamatan(request):
    ormas = Ormas.objects.values('kecamatan').filter(status = '1').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'frontend/ormas_kec.html', konteks)

def ormasKabupaten(request):
    ormas = Ormas.objects.values('kabupaten').filter(status = '1').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'frontend/ormas_kab.html', konteks)

def grafik(request):
    unsur = Ormas.objects.values('unsur').filter(status = '1').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')
    desa = Ormas.objects.values('desa').filter(status = '1').annotate(
        jumlah=Count('desa')
    ).order_by('desa')
    kecamatan = Ormas.objects.values('kecamatan').filter(status = '1').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')
    kabupaten = Ormas.objects.values('kabupaten').filter(status = '1').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'unsur':unsur,
                'desa':desa,
                'kecamatan':kecamatan,
                'kabupaten':kabupaten,
        }

    return render(request, 'frontend/grafik.html', konteks)

def galeriView(request):
    galeri = Galeri.objects.all()

    konteks = {
        'galeri' : galeri,
    }
    return render(request, 'frontend/galeri.html', konteks)


def statistik(request):
    data = Ormas.objects.all()

    #maesan
    maesanPendidikan = data.filter(kecamatan="MAESAN", unsur="Pendidikan", status = '1').count()
    maesanPolitik = data.filter(kecamatan="MAESAN", unsur="Politik", status = '1').count()
    maesanSosial = data.filter(kecamatan="MAESAN", unsur="Sosial", status = '1').count()
    maesanEkonomi = data.filter(kecamatan="MAESAN", unsur="Ekonomi", status = '1').count()
    maesanLainnya = data.filter(kecamatan="MAESAN", unsur="Lainnya", status = '1').count()

    #grujugan
    grujuganPendidikan = data.filter(kecamatan="GRUJUGAN", unsur="Pendidikan", status = '1').count()
    grujuganPolitik = data.filter(kecamatan="GRUJUGAN", unsur="Politik", status = '1').count()
    grujuganSosial = data.filter(kecamatan="GRUJUGAN", unsur="Sosial", status = '1').count()
    grujuganEkonomi = data.filter(kecamatan="GRUJUGAN", unsur="Ekonomi", status = '1').count()
    grujuganLainnya = data.filter(kecamatan="GRUJUGAN", unsur="Lainnya", status = '1').count()

    #tamanan
    tamananPendidikan = data.filter(kecamatan="TAMANAN", unsur="Pendidikan", status = '1').count()
    tamananPolitik = data.filter(kecamatan="TAMANAN", unsur="Politik", status = '1').count()
    tamananSosial = data.filter(kecamatan="TAMANAN", unsur="Sosial", status = '1').count()
    tamananEkonomi = data.filter(kecamatan="TAMANAN", unsur="Ekonomi", status = '1').count()
    tamananLainnya = data.filter(kecamatan="TAMANAN", unsur="Lainnya", status = '1').count()

    #jambesari ds
    jambesariPendidikan = data.filter(kecamatan="JAMBESARI", unsur="Pendidikan", status = '1').count()
    jambesariPolitik = data.filter(kecamatan="JAMBESARI", unsur="Politik", status = '1').count()
    jambesariSosial = data.filter(kecamatan="JAMBESARI", unsur="Sosial", status = '1').count()
    jambesariEkonomi = data.filter(kecamatan="JAMBESARI", unsur="Ekonomi", status = '1').count()
    jambesariLainnya = data.filter(kecamatan="JAMBESARI", unsur="Lainnya", status = '1').count()

    #pujer
    pujerPendidikan = data.filter(kecamatan="PUJER", unsur="Pendidikan", status = '1').count()
    pujerPolitik = data.filter(kecamatan="PUJER", unsur="Politik", status = '1').count()
    pujerSosial = data.filter(kecamatan="PUJER", unsur="Sosial", status = '1').count()
    pujerEkonomi = data.filter(kecamatan="PUJER", unsur="Ekonomi", status = '1').count()
    pujerLainnya = data.filter(kecamatan="PUJER", unsur="Lainnya", status = '1').count()

    konteks ={
        'maesanPendidikan':maesanPendidikan,
        'maesanPolitik':maesanPolitik,
        'maesanSosial':maesanSosial,
        'maesanEkonomi':maesanEkonomi,
        'maesanLainnya':maesanLainnya,

        'grujuganPendidikan':grujuganPendidikan,
        'grujuganPolitik':grujuganPolitik,
        'grujuganSosial':grujuganSosial,
        'grujuganEkonomi':grujuganEkonomi,
        'grujuganLainnya':grujuganLainnya,

        'tamananPendidikan':tamananPendidikan,
        'tamananPolitik':tamananPolitik,
        'tamananSosial':tamananSosial,
        'tamananEkonomi':tamananEkonomi,
        'tamananLainnya':tamananLainnya,

        'jambesariPendidikan':jambesariPendidikan,
        'jambesariPolitik':jambesariPolitik,
        'jambesariSosial':jambesariSosial,
        'jambesariEkonomi':jambesariEkonomi,
        'jambesariLainnya':jambesariLainnya,

        'pujerPendidikan':pujerPendidikan,
        'pujerPolitik':pujerPolitik,
        'pujerSosial':pujerSosial,
        'pujerEkonomi':pujerEkonomi,
        'pujerLainnya':pujerLainnya,

    }

    return render(request, 'backend/statistik.html', konteks)



@login_required(login_url='login')
def dataOrmas(request):
    ormas = Ormas.objects.filter(status= '1')
    unverormas = Ormas.objects.filter(status = '0')

    konteks ={
        'ormas':ormas,
        'unverormas' : unverormas,
    }

    return render(request, 'backend/data_ormas.html', konteks)


@login_required(login_url='login')
def hapusOrmas(request, id_ormas):
    ormas = Ormas.objects.get(id=id_ormas)
    ormas.delete()

    return redirect('data_ormas')


def publishOrmas(request, id_ormas):
    ormas = Ormas.objects.get(id=id_ormas)

    ormas.status = '1'
    ormas.save()

    return redirect('data_ormas')


@login_required(login_url='login')
def tambahOrmas(request):
    if request.POST :
        form = FormOrmas(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data telah berhasil dikirim, mohon menunggu verifikasi admin untuk pengecekan data anda !!!'
            form = FormOrmas

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/add_data_ormas.html', konteks)

    else:
            form = FormOrmas()

            konteks ={
                'form':form,
            }

    return render(request, 'backend/add_data_ormas.html', konteks)


@login_required(login_url='login')
def editOrmas(request, id_ormas):
    data_ormas = Ormas.objects.get(id=id_ormas)
    template = 'backend/edit_data_ormas.html'
    if request.POST:
        form = FormOrmas(request.POST,request.FILES, instance=data_ormas)
        if form.is_valid():
            form.save()
            return redirect('edit_ormas', id_ormas=id_ormas)
    else:
        form = FormOrmas(instance=data_ormas)
        konteks ={
            'form':form,
            'data_ormas':data_ormas,
        }
        return render(request, template, konteks)

@login_required(login_url='login')
def jmlOrmasUnsur(request):
    ormas = Ormas.objects.values('unsur').filter(status = '1').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_uns.html', konteks)

@login_required(login_url='login')
def jmlOrmasDesa(request):
    ormas = Ormas.objects.values('desa').filter(status = '1').annotate(
        jumlah=Count('desa')
    ).order_by('desa')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_ds.html', konteks)

@login_required(login_url='login')
def jmlOrmasKecamatan(request):
    ormas = Ormas.objects.values('kecamatan').filter(status = '1').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_kec.html', konteks)

@login_required(login_url='login')
def jmlOrmasKabupaten(request):
    ormas = Ormas.objects.values('kabupaten').filter(status = '1').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_kab.html', konteks)

@login_required(login_url='login')
def galeri(request):
    galeri = Galeri.objects.all()

    konteks = {
        'galeri' : galeri,
    }
    return render(request, 'backend/galeri.html', konteks)

@login_required(login_url='login')
def tambahGaleri(request):
    if request.POST:
        form = FormGaleri(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormGaleri

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_galeri.html', konteks)

    else:
        form = FormGaleri()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_galeri.html', konteks)

@login_required(login_url='login')
def hapusGaleri(request, id_galeri):
    pohon = Galeri.objects.get(id=id_galeri)
    pohon.delete()

    return redirect('galeri')

@login_required(login_url='login')
def editGaleri(request, id_galeri):
    galeri = Galeri.objects.get(id=id_galeri)
    template = 'backend/edit_galeri.html'
    if request.POST:
        form = FormGaleri(request.POST,request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            return redirect('galeri')
    else:
        form = FormGaleri(instance=galeri)
        konteks ={
            'form':form,
            'galeri':galeri,
        }
        return render(request, template, konteks)

@login_required(login_url='login')
def informasi(request):
    informasi = Informasi.objects.all()

    konteks ={
        'informasi':informasi,
    }
    return render(request, 'backend/informasi.html', konteks)

@login_required(login_url='login')
def tambahInformasi(request):
    if request.POST:
        form = FormInformasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormInformasi

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_informasi.html', konteks)

    else:
        form = FormInformasi()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_informasi.html', konteks)

@login_required(login_url='login')
def hapusInformasi(request, id_informasi):
    informasi = Informasi.objects.get(id=id_informasi)
    informasi.delete()

    return redirect('informasi')

@login_required(login_url='login')
def editInformasi(request, id_informasi):
    informasi = Informasi.objects.get(id=id_informasi)
    template = 'backend/edit_informasi.html'
    if request.POST:
        form = FormInformasi(request.POST,request.FILES, instance=informasi)
        if form.is_valid():
            form.save()
            return redirect('informasi')
    else:
        form = FormInformasi(instance=informasi)
        konteks ={
            'form':form,
            'informasi':informasi,
        }
        return render(request, template, konteks)

@login_required(login_url='login')
def daftarUser(request):
    user = User.objects.all()

    konteks = {
        'user' : user,
    }
    return render(request, 'backend/daftar_user.html', konteks)

def del_user(request, id):    
    try:
        u = User.objects.get(id = id)
        u.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return render(request, 'backend/daftar_user.html')

    except Exception as e: 
        return render(request, 'backend/daftar_user.html')

    return render(request, 'backend/daftar_user.html')
    


def pendaftaran(request):
    return render(request, 'backend/pendaftaran.html')


@login_required
def daftar(request):
    if request.method == 'POST':
        
        user_form = FormUser(request.POST, instance=request.user)
        ormas = FormOrmas(request.POST, request.FILES, instance=request.user.ormas)
        if user_form.is_valid() and ormas.is_valid():
            user_form.save()
            ormas.status = '0'
            ormas.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='logout')
    else:
        user_form = FormUser(instance=request.user)
        ormas = FormOrmas(instance=request.user.ormas)


    return render(request, 'backend/daftar.html', {'user_form': user_form, 'ormas': ormas})

    