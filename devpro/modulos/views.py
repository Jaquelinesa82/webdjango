from django.shortcuts import render

from devpro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulos(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
