from django.contrib import admin

from .models import Recebimento
from .models import Despesas

admin.site.register(Recebimento)
admin.site.register(Despesas)
