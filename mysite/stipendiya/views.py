from django.shortcuts import render, redirect
from .models import Talaba
from .forms import TalabaForm


def home(request):
    model = Talaba()
    form = TalabaForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'index.html', ctx)

def adminstrator(request):
    return render(request,'admins.html')
