from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
# class businessleadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     ...
# admin.site.register(businesslead, businessleadAdmin)

admin.site.register(invoice)
admin.site.register(receipt)
admin.site.register(implementation)