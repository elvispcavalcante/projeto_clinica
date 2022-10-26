from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Paciente
from django import forms

COMORBIDADE_CHOICES = (
    (u'1', u'Sim'),
    (u'0', u'Não'),
)


class PacienteCadastroForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome', 'cpf', 'sexo', 'endereco', 'comorbidade', 'info_comorbidade', 'telefone', 'data_nascimento')
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'endereco': 'Endereço Completo',
            'comorbidade': 'Comorbidade',
            'info_comorbidade': 'Informações das Comorbidades',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do Paciente'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Digite o CPF do Paciente'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Digite o Endereço Completo'}),
            'comorbidade': forms.RadioSelect(choices=COMORBIDADE_CHOICES),
            'data_nascimento': forms.DateInput(format='%d/%m/%Y')
        }

