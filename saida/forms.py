from django import forms
from .models import SaidaProduto, Produto
from django.utils import timezone
class SaidaProdutoForm(forms.ModelForm):
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.Select(attrs={'class': 'input'}),
        label='Produto'
    )

    class Meta:
        model = SaidaProduto
        fields = ['produto', 'quantidade', 'data_saida']

        widgets = {
            'quantidade': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite a quantidade do produto'}),
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        # Preenche o campo data_saida com a data e hora atuais antes de salvar
        self.instance.data_saida = timezone.now()

        return super(SaidaProdutoForm, self).save(commit)
