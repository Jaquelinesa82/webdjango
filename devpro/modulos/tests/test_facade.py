import pytest
from model_bakery import baker
from devpro.modulos import facade
from devpro.modulos.models import Modulo


@pytest.fixture()
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in 'antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
