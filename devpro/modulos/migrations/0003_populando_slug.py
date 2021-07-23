# Generated by Django 3.2.5 on 2021-07-23 01:05

from django.db import migrations
from django.utils.text import slugify


def popular_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]
