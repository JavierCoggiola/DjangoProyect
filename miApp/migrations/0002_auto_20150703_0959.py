# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del comentario')),
            ],
        ),
        migrations.RenameModel(
            old_name='Entrada',
            new_name='Noticia',
        ),
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mi Noticia', 'verbose_name_plural': 'Todas mis noticias'},
        ),
        migrations.AddField(
            model_name='coment',
            name='postDelComent',
            field=models.ForeignKey(to='miApp.Noticia'),
        ),
    ]
