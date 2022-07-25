from django.contrib import admin

from .models import Conta
from .models import Despesa
from .models import Resultado

admin.site.register(Conta)
admin.site.register(Despesa)
admin.site.register(Resultado)
