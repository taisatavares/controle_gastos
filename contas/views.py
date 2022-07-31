from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Conta
from .models import Despesa
from .models import Resultado
from decimal import Decimal


def contaList(request):
    contas = Conta.objects.all()
    despesas = Despesa.objects.all()
    resultado = calcula_resultado(contas, despesas)
    return render(request, 'contas/list.html', {'contas': contas, 'despesas': despesas, 'resultado_final': resultado})


def calcula_resultado(contas: list[Conta], despesas: list[Despesa]):
    receita_total = Decimal()
    for conta in contas:
        receita_total += conta.valor

    for despesa in despesas:
        receita_total -= despesa.valor

    return receita_total


def contaView(request, id):
    conta = get_object_or_404(Conta, pk=id)
    return render(request, 'contas/conta.html', {'conta': conta})

def despesaView(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    return render(request, 'contas/despesa.html', {'despesa': despesa})


def helloWorld(request):
    return HttpResponse('Hello World!')


def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name': name})
