from django import forms
from .models import EntradaProduto

class EntradaProdutoForm(forms.ModelForm):
    class Meta:
        model = EntradaProduto
        fields = ['produto', 'quantidade']
