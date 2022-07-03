from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('Hello World!')

def contaList(request):
    return render(request, 'contas/list.html')

def yourName(request, name):
    return render(request, 'contas/yourname.html', {'name':name})
