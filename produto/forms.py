from django import forms
from .models import Produto

class ProdutoListForm(forms.Form):

    filtro_num_choices = (
        ('td', 'Todos os Produtos'),
        ('abaixo', 'Abaixo da quantidade mínima'),
        ('acima', 'Acima da quantidade mínima'),
    )

    filtro_num = forms.ChoiceField(label='Filtro de  numero produto:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=filtro_num_choices, required=False)

    quantidade = forms.IntegerField(label='Quantidade:', widget=forms.NumberInput(
        attrs={'class': 'input', 'placeholder': 'Digite a quantidade do produto'}), required=False)

    quantidademin = forms.IntegerField(label='Quantidade mínima:', widget=forms.NumberInput(
        attrs={'class': 'input', 'placeholder': 'Digite a quantidade mínima do produto'}), required=False)

    buscar = forms.CharField(label='Buscar:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o nome ou código do produto'}), required=False)

    nome = forms.CharField(label='Nome:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o nome do produto'}), required=False)

    codigo = forms.CharField(label='Código:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o código do produto'}), required=False)


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

