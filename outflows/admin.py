from django.contrib import admin
from . import models


class OutFlowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'update_at',)
    search_fields = ('product__title',)


admin.site.register(models.Outflow, OutFlowAdmin)
