from django.urls import reverse
from devpro.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>DevPro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">DevPro</a>')


def test_email_link(resp):
    assert_contains(resp, f'href="mailto:jaquelinesa.82@gmail.com"')
