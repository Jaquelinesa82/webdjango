# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>EM MANUTENÇÃO</body></html>', content_type='text/html')
