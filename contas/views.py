from django.shortcuts import render
from django.http import HttpResponse
from .models import Conta
from .models import Despesa

def contaList(request):
    contas = Conta.objects.all()
    despesas = Despesa.objects.all()
    return render(request, 'contas/list.html', {'contas':contas, 'despesas':despesas})


def helloWorld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name':name})
