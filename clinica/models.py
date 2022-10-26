from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cpf_cnpj.fields import CPFField

SEXO_CHOICES = (
    ('F', 'Feminino'),
    ('M', 'Masculino'),
)

COMORBIDADE_CHOICES = (
    (u'1', u'Sim'),
    (u'0', u'Não'),
)


class Usuario(AbstractUser):
    cpf = CPFField(masked=True)


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField(masked=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.CharField(max_length=100)
    comorbidade = models.CharField(choices=COMORBIDADE_CHOICES, max_length=1)
    info_comorbidade = models.TextField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(format('%d/%m/%Y'))
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + ' - ' + self.cpf

    class Meta:
        ordering = ['nome']


class Especialidade(models.Model):
    especialidade = models.CharField(max_length=80)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.especialidade

    class Meta:
        ordering = ['especialidade']


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField(masked=True)
    crm = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + ' - ' + self.cpf

    class Meta:
        ordering = ['nome']


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_consulta = models.DateField(format('%d/%m/%Y'))
    prontuario = models.TextField()
    receituario = models.TextField()
    ddata_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data_consulta + ' - ' + self.paciente.nome + ' - ' + self.medico.nome

    class Meta:
        ordering = ['paciente']




