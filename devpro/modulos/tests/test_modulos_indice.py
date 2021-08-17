from typing import List

from django.urls import reverse
from devpro.django_assertions import assert_contains
import pytest
from model_bakery import baker

from devpro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas=[]
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return  aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulo(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_publico(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_aulas_titulos(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_urls(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())