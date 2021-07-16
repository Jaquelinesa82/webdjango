import pytest
from django.urls import reverse
from devpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos: indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: App',
        'Video Aperitivo: Automacao',
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)

#
# def test_conteudo_video(resp):
#     assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/9iZLDnW_vwU"')
