from django.urls import path
from .import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.contaList, name='conta-list'),
    path('conta/<int:id>', views.contaView, name="conta-view"),
    path('despesa/<int:id>', views.despesaView, name="despesa-view"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]