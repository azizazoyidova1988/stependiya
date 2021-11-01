from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from stipendiya.forms import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):

    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def talaba_list(request):
    talaba = services.get_talaba()
    ctx = {
        "talaba": talaba
    }
    return render(request, 'dashboard/talaba/list.html', ctx)


@login_required_decorator
def talaba_create(request):
    model = Talaba()
    form = TalabaForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('talaba_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/talaba/form.html', ctx)


@login_required_decorator
def otm_list(request):
    otm = services.get_otm()
    ctx = {
        "otm": otm
    }
    return render(request, 'dashboard/otm/list.html', ctx)


@login_required_decorator
def otm_create(request):
    model = OTM()
    form = OTMForm(request.POST, request.FILES,instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('otm_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/otm/form.html', ctx)

@login_required_decorator
def status(request, pk, status):
    model = Ariza_statusi.objects.get(id=pk)
    model.status = status
    model.save()
    return redirect("ariza_status_list")


@login_required_decorator
def ariza_status_list(request):
    status = services.get_status_info([1, 2, 3, 4, 5, 6, 7, 8])
    filter = "all"
    if request.POST:
        filter = request.POST.get("order_filter")

        if filter == "ariza_yuborildi":
            status = services.get_status_info([2])

        if filter == "korib_chiqilmoqda":
            status = services.get_status_info([3])

        if filter == "qabul_qilindi":
            status = services.get_status_info([4])

        if filter == "vazirlikka_yuborildi":
            status = services.get_status_info([5])

        if filter == "vazirlik_koryapti":
            status = services.get_status_info([6])

        if filter == "tavsiya_etildi":
            status = services.get_status_info([7])

        if filter == "tavsiya_etilmadi":
            status = services.get_status_info([8])

    ctx = {
        "status": status,
        "filter": filter,
    }
    return render(request, 'dashboard/ariza_statusi/list.html', ctx)



@login_required_decorator
def talaba_xisoboti_list(request):
    talaba_xisoboti = services.get_talaba_by_otm()
    ctx = {
        "talaba_xisoboti": talaba_xisoboti
    }
    return render(request, 'dashboard/talaba_xisoboti/list.html', ctx)


@login_required_decorator
def talaba_faoliyati_list(request):
    talaba_faoliyati = services.get_talaba_faoliyati()
    ctx = {
        "talaba_faoliyati": talaba_faoliyati
    }
    return render(request, 'dashboard/talaba_faoliyati/list.html', ctx)


@login_required_decorator
def yangi_ariza_list(request):
    yangi_ariza = services.get_yangi_ariza()
    ctx = {
        "yangi_ariza": yangi_ariza
    }
    return render(request, 'dashboard/yangi_ariza/list.html', ctx)

@login_required_decorator
def adminstrator_list(request):
    adminstrator = services.get_adminstrator()
    ctx = {
        "adminstrator": adminstrator
    }
    return render(request, 'dashboard/adminstrator/list.html', ctx)


@login_required_decorator
def adminstrator_create(request):
    model = Administrator_royxati()
    form = AdminstratorForm(request.POST, request.FILES,instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('adminstrator_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/adminstrator/form.html', ctx)


