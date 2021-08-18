from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from devpro.modulos import facade


def indice(requests):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(requests, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulos(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
