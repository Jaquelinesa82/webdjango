from devpro.modulos.models import Modulo, Aula
from typing import List


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulos(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulos_ordenados(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    return Modulo.objects.order_by('order').all()