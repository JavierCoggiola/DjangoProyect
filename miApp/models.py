# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Noticia(models.Model):
    class Meta:
        verbose_name = "Mi Noticia"
        verbose_name_plural = "Todas mis noticias"
        ordering=['-fecha']
    
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    autor = models.ForeignKey(User)
    
    def __str__(self):
        return self.titulo
    
class Coment(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    mail = models.CharField(u'Mail', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    postDelComent = models.ForeignKey(Noticia)
    fecha = models.DateTimeField(u'Fecha del comentario',auto_now_add=True)
    def __str__(self):
        return "Nombre: "+self.nombre+" / Mensaje: "+self.mensaje