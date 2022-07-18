from django.contrib import admin

from .models import Conta
from .models import Despesa

admin.site.register(Conta)
admin.site.register(Despesa)

