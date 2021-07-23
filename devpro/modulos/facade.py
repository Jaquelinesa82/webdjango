from devpro.modulos.models import Modulo
from typing import List


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulos(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)