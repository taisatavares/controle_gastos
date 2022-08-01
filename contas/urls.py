from django.urls import path
from .import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.contaList, name='conta-list'),
    path('conta/<int:id>', views.contaView, name="conta-view"),
    path('despesa/<int:id>', views.despesaView, name="despesa-view"),
    path('newconta/', views.newConta, name="nova-conta"),
    path('newdespesa/', views.newDespesa, name="nova-despesa"),
    path('edit/<int:id>', views.editConta, name="edit-conta"),
    path('edicao/<int:id>', views.edicaoDespesa, name="edicao-conta"),
    path('delete/<int:id>', views.deleteConta, name="delete-conta"),
    path('deletar/<int:id>', views.deletarDespesa, name="deletar-despesa"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]