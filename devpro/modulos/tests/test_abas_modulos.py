from django.urls import reverse
from devpro.django_assertions import assert_contains
import pytest
from model_bakery import baker

from devpro.modulos.models import Modulo


@pytest.fixture()
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulos.titulo)


def test_link_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulos.get_absolute_url())
