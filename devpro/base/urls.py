from django.urls import path
from devpro.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]