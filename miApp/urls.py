from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'miApp.views.home', name='home'),
                       url(r'^Cronometro/$', 'miApp.views.crono', name='crono'),
                       url(r'^AzarImagenes/$', 'miApp.views.img', name='img'),
                       url(r'^CurriculumJavier/$', 'miApp.views.curr', name='curr'),
                       url(r'^Calculadora/$', 'miApp.views.calcu', name='calcu'),
                       url(r'^ConversorDeUnidades/$', 'miApp.views.conver', name='conver'),
                       url(r'^Cuestionario/$', 'miApp.views.cuest', name='cuest'),
                       url(r'^ContactoJavier/$', 'miApp.views.contact', name='contact'),
                       url(r'^verNoticia/(?P<id_post>[0-9]+)/$', 'miApp.views.verNoticia', name='vermipost'),
                       url(r'^Comentarios/$', 'miApp.views.guardar_mensaje', name='comentarios'),
                       url(r'^SendingMail/$', 'miApp.views.sendMail', name='sendMail'),
                      )