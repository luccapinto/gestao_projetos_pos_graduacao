# projetos/forms.py

from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'arquivo']

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if arquivo:
            if arquivo.size > 10 * 1024 * 1024:
                raise forms.ValidationError('O arquivo não pode exceder 10MB.')
            if not arquivo.name.endswith(('.pdf', '.docx')):
                raise forms.ValidationError('Formato de arquivo não suportado.')
        return arquivo
