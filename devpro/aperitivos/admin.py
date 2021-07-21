from django.contrib.admin import ModelAdmin, register
from devpro.aperitivos.models import Video



@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('slug', 'titulo', 'creation', 'youtube_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulo',)}
