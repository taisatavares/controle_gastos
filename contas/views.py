from django.shortcuts import render
from django.http import HttpResponse
from .models import Conta
from .models import Despesa

def contaList(request):
    contas = Conta.objects.all()
    return render(request, 'contas/list.html', {'contas':contas})

def despesaList(request):
    despesas = Despesa.objects.all()
    return render(request, 'contas/list.html', {'despesas':despesas})


def helloWorld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name':name})
