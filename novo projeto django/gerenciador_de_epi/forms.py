# gerenciador_de_epi/forms.py

from django import forms
# Importe o modelo que o formulário irá manipular
from .models import Colaborador

# Cria a classe de formulário baseada no modelo Colaborador
class ColaboradorForm(forms.ModelForm):
    class Meta:
        # 1. Diz ao Django qual modelo usar como base
        model = Colaborador
        
        # 2. Especifica quais campos do modelo devem aparecer no formulário
        fields = ['nome_completo', 'matricula', 'setor']
        
        # Opcional: Personaliza os rótulos (labels)
        labels = {
            'nome_completo': 'Nome Completo do Colaborador',
            'matricula': 'Número de Matrícula',
            'setor': 'Setor/Departamento',
        }