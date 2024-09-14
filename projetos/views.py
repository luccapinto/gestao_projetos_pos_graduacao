# projetos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ProjetoForm
from django.utils import timezone

def periodo_submissao_aberto():
    # Exemplo: período de submissão de 1º de janeiro a 31 de março
    hoje = timezone.now().date()
    inicio = timezone.datetime(hoje.year, 1, 1).date()
    fim = timezone.datetime(hoje.year, 3, 31).date()
    return inicio <= hoje <= fim

@login_required
def dashboard(request):
    if request.user.user_type == 'aluno':
        return redirect('lista_projetos')
    elif request.user.user_type == 'avaliador':
        return redirect('lista_turmas')

@login_required
def lista_projetos(request):
    projetos = Projeto.objects.filter(aluno=request.user).order_by('-data_submissao')
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

@login_required
def submeter_projeto(request):
    if not periodo_submissao_aberto():
        return render(request, 'projetos/fora_do_periodo.html')
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.aluno = request.user
            projeto.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/submeter_projeto.html', {'form': form})

@login_required
def detalhes_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, aluno=request.user)
    return render(request, 'projetos/detalhes_projeto.html', {'projeto': projeto})

@login_required
def historico_notas(request):
    projetos = Projeto.objects.filter(aluno=request.user, nota__isnull=False).order_by('-ciclo')
    return render(request, 'projetos/historico_notas.html', {'projetos': projetos})
