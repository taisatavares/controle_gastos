from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Conta
from .models import Despesa
from .models import Resultado
from decimal import Decimal
from .forms import ContaForm
from .forms import DespesaForm


def contaList(request):
    contas = Conta.objects.all().order_by('-created_at')
    despesas = Despesa.objects.all().order_by('-created_at')
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

def newConta(request):
    if request.method == 'POST':
          form = ContaForm(request.POST)

          if form.is_valid():
              Conta = form.save()
              return redirect('/')
    else:
        form = ContaForm()
        return render(request, 'contas/addconta.html', {'form': form})

def newDespesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            Despesa = form.save()
            return redirect('/')
    else:
        form = DespesaForm()
        return render(request, 'contas/adddespesa.html', {'form': form})

def editConta(request, id):
    conta = get_object_or_404(Conta, pk=id)
    form = ContaForm(instance=conta)

    if(request.method == 'POST'):
        form = ContaForm(request.POST, instance=conta)

        if(form.is_valid()):
            conta.save()
            return redirect('/')
        else:
            return render(request, 'contas/editconta.html', {'form': form, 'conta': conta})
    else:
        return render(request, 'contas/editconta.html', {'form': form, 'conta': conta})

def edicaoDespesa(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    form = DespesaForm(instance=despesa)

    if (request.method == 'POST'):
        form = DespesaForm(request.POST, instance=despesa)

        if (form.is_valid()):
            despesa.save()
            return redirect('/')
        else:
            return render(request, 'contas/edicaodespesa.html', {'form': form, 'despesa': despesa})
    else:
        return render(request, 'contas/edicaodespesa.html', {'form': form, 'despesa': despesa})

def helloWorld(request):
    return HttpResponse('Hello World!')


def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name': name})
