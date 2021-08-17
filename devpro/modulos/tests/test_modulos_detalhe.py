from django.urls import reverse
from devpro.django_assertions import assert_contains
import pytest
from model_bakery import baker

from devpro.modulos.models import Modulo


@pytest.fixture()
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture()
def aulas(modulo):
    return baker.make(aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_aulas_titulos(resp, aulas):
    assert_contains(resp, aula.titulo)
