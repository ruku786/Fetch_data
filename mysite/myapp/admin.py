from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import employee

@admin.register(employee)
class ViewAdmin(ImportExportModelAdmin):
    pass
   # list_display = ('name', 'emailid', 'phoneno')

