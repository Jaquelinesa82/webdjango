from django.shortcuts import render

from devpro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulos(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})
