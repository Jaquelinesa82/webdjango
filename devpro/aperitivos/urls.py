from django.urls import path

from devpro.aperitivos.views import video

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
