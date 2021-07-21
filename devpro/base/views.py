from django.shortcuts import render

from devpro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {})
