from django import forms
from .models import EntradaProduto, Produto
from django.utils import timezone


class EntradaProdutoForm(forms.ModelForm):
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.Select(attrs={'class': 'input'}),
        label='Produto'
    )

    class Meta:
        model = EntradaProduto
        fields = ['produto', 'quantidade', 'data_entrada']

        widgets = {
            'quantidade': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite a quantidade do produto'}),
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        # Preenche o campo data_saida com a data e hora atuais antes de salvar
        self.instance.data_entrada = timezone.now()

        return super(EntradaProdutoForm, self).save(commit)
