from django.shortcuts import render
from django.http import HttpResponse
from .models import Conta
from .models import Despesa
from .models import Resultado

def contaList(request):
    contas = Conta.objects.all()
    despesas = Despesa.objects.all()
    resultados = Resultado.objects.all()
    return render(request, 'contas/list.html', {'contas':contas, 'despesas':despesas, 'resultados':resultados})


def helloWorld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name':name})
