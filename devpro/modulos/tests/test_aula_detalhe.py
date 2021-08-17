from django.urls import reverse
from devpro.django_assertions import assert_contains
import pytest
from model_bakery import baker

from devpro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_youtube(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.youtube_id }"')


