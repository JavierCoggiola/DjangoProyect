from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect

from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from miApp.models import Noticia, Coment

# Create your views here.

def home(request):
    context = RequestContext(request)
    posts = Noticia.objects.all
    return render_to_response('home.html',
                              {'posts':posts},
                              context)
def crono(request):
    context = RequestContext(request)
    return render_to_response('crono.html',
                              context)
def img(request):
    context = RequestContext(request)
    return render_to_response('azar.html',
                              context)
def conver(request):
    context = RequestContext(request)
    return render_to_response('conversor.html',
                              context)

def cuest(request):
    context = RequestContext(request)
    return render_to_response('cuestionario.html',
                              context)

def curr(request):
    context = RequestContext(request)
    return render_to_response('curriculum.html',
                              context)

def calcu(request):
    context = RequestContext(request)
    return render_to_response('calculo.html',
                              context)

def contact(request):
    context = RequestContext(request)
    return render_to_response('contacto.html',
                              context)

def sendMail(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        
        nombre= request.POST['nombre']
        direcMail= request.POST['direcMail']
        msj= request.POST['msj']
        
        subject = 'Mensaje de JaviBlog de: '+nombre
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(subject, msj, from_email,
    [direcMail], fail_silently=False)
        
    return render_to_response('contacto.html',
                              context)

def verNoticia(request, id_post):
    context = RequestContext(request)
    mi_post = Noticia.objects.get(id=id_post)
    
    if request.method == 'POST':
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Coment()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.postDelComent = mi_post
        msje.save()
    
    msjs = Coment.objects.filter(postDelComent=mi_post)
    
    return render_to_response('post.html', 
                              {'post':mi_post,
                              'msjs':msjs},
                              context)

def guardar_mensaje(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        print(123)
        mi_post = Noticia.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Coment()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.postDelComent = mi_post
        msje.save()
        msjs = Coment.objects.filter(postDelComent=mi_post)
    
    return render_to_response('mensajes.html', 
                              {'msjs':msjs},
                              context)