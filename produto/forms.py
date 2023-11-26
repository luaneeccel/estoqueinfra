from django import  forms
from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model=Produto
        fields=['foto', 'codigo', 'nome', 'observacao', 'tipo', 'quantidademin', 'quantidade', 'unidade']

        widgets = {
            'nome': forms.TextInput(
                attrs={'class':'input','type':'text', 'placeholder':'Digite o nome do Produto'}),

            'observacao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o endereco do produto'}),
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o codigo do produto'}),
            'foto':forms.FileInput(attrs={'class':'input', 'type':'file'}),
            'quantidade': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite a quantidade do produto'}),

            'quantidademin': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite a quantidade mínima do produto'}),

            'unidade': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a unidade do produto'}),
        }

