# projetos/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class Projeto(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='projetos/')
    data_submissao = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('submetido', 'Submetido'),
        ('em_avaliacao', 'Em Avaliação'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('revisao', 'Em Revisão'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='submetido')
    ciclo = models.IntegerField(default=timezone.now().year)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
