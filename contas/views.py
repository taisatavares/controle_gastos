from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Conta
from .models import Despesa
from .models import Resultado
from decimal import Decimal
from .forms import ContaForm
from .forms import DespesaForm
from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def contaList(request):
    contas = Conta.objects.all().order_by('-created_at')
    despesas_list = Despesa.objects.all().order_by('-created_at')
    paginator = Paginator(despesas_list, 4)
    page = request.GET.get('page')
    despesas = paginator.get_page(page)
    resultado = calcula_resultado(contas, despesas_list)


    search = request.GET.get('search')



    if search:

        despesas = Despesa.objects.filter(titulo__icontains=search)

    else:

        despesas_list = Despesa.objects.all().order_by('-created_at')
        paginator = Paginator(despesas_list,4)
        page = request.GET.get('page')
        despesas = paginator.get_page(page)


    return render(request, 'contas/list.html', {'contas': contas, 'despesas': despesas, 'resultado_final': resultado})


def calcula_resultado(contas: list[Conta], despesas: list[Despesa]):
    receita_total = Decimal()
    for conta in contas:
        receita_total += conta.valor

    for despesa in despesas:
        receita_total -= despesa.valor

    return receita_total

@login_required
def contaView(request, id):
    conta = get_object_or_404(Conta, pk=id)
    return render(request, 'contas/conta.html', {'conta': conta})

@login_required
def despesaView(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    return render(request, 'contas/despesa.html', {'despesa': despesa})

@login_required
def newConta(request):
    if request.method == 'POST':
          form = ContaForm(request.POST)

          if form.is_valid():
              Conta = form.save()
              return redirect('/')
    else:
        form = ContaForm()
        return render(request, 'contas/addconta.html', {'form': form})

@login_required
def newDespesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            Despesa = form.save()
            return redirect('/')
    else:
        form = DespesaForm()
        return render(request, 'contas/adddespesa.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def deleteConta(request, id):
    conta = get_object_or_404(Conta, pk=id)
    conta.delete()

    messages.info(request, 'Receita deletada com sucesso')

    return redirect('/')

@login_required
def deletarDespesa(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    despesa.delete()

    messages.info(request, 'Despesa deletada com sucesso')

    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World!')


def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name': name})
