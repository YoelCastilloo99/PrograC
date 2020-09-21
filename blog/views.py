# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})
