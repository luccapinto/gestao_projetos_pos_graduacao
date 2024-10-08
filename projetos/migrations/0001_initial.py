# Generated by Django 5.1.1 on 2024-09-14 03:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('arquivo', models.FileField(upload_to='projetos/')),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('submetido', 'Submetido'), ('em_avaliacao', 'Em Avaliação'), ('aprovado', 'Aprovado'), ('rejeitado', 'Rejeitado'), ('revisao', 'Em Revisão')], default='submetido', max_length=20)),
                ('ciclo', models.IntegerField(default=2024)),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
