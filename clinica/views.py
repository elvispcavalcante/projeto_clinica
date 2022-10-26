from django.views.generic import FormView, TemplateView, UpdateView, CreateView, ListView, DetailView, DeleteView
from .forms import PacienteCadastroForm
from django.urls import reverse_lazy


# Create your views here.
class CadastroPaciente(CreateView):
    template_name = 'cadastro_paciente.html'
    form_class = PacienteCadastroForm
    success_url = reverse_lazy('clinica:cadastro_paciente')