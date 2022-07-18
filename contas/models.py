from django.db import models
from django.contrib.auth import get_user_model

class Conta(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} - {self.valor}'


class Despesa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} - {self.valor}'

class Resultado(models.Model):
    titulo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} - {self.valor}'
