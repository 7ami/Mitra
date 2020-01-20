from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Accommo

# Register your models here.


@admin.register(Accommo)
class ViewAdmin(ImportExportModelAdmin):
    pass
