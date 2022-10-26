from django.contrib import admin
from .models import Usuario, Paciente, Especialidade, Medico, Consulta
from django.contrib.auth.admin import UserAdmin

# Inserir informações de usuário customizado na Administração do Django
campos = list(UserAdmin.fieldsets)
campos.append(
    ('Dados Pessoais', {'fields': ('cpf',)})
)
UserAdmin.fieldsets = tuple(campos)
# Fim das informações de Usuário Customizado


# Para inserção de outras tabelas é necessário criar classes
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'sexo', 'endereco', 'comorbidade', 'info_comorbidade', 'telefone', 'data_nascimento']
    search_fields = ['nome', 'cpf', 'comorbidade', 'endereco']
    list_per_page = 10


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['especialidade']
    search_fields = ['especialidade']
    list_per_page = 10


class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'crm', 'endereco', 'especialidade']
    search_fields = ['nome', 'cpf']
    list_per_page = 15


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'data_consulta', 'prontuario', 'receituario']
    search_fields = ['paciente', 'medico', 'data_consulta']
    list_per_page = 15


# Registrando Modelos na Administração do Django
admin.site.register(Usuario, UserAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Consulta, ConsultaAdmin)

