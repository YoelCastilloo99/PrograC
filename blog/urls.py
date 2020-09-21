from django.conf.urls import url 
from . import views

urlpatterns = [
    url('', views.publicacion_lista, name='publicacion_lista'),
]