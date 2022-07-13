from django.contrib import admin

from .models import Recebimento
from .models import Despesas
from .models import Resultado

admin.site.register(Recebimento)
admin.site.register(Despesas)
admin.site.register(Resultado)

