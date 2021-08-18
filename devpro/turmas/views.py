from django.shortcuts import render


def indice(requests):
    return render(requests, 'turmas/indice.html')
