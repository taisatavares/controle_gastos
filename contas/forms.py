from django import forms
from .models import Conta
from .models import Despesa

class ContaForm(forms.ModelForm):

    class Meta:
        model = Conta
        fields = ('titulo', 'descricao', 'valor')

class DespesaForm(forms.ModelForm):

    class Meta:
        model = Despesa
        fields = ('titulo', 'descricao', 'valor')