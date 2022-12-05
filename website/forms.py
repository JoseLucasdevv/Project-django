from django.forms import ModelForm
from project.models import Funcionario

# Create the form class.
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            "nome",
            "sobrenome",
            "cpf",
            "tempo_de_servico",
            "remuneracao",
        ]
