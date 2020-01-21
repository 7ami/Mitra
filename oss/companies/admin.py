from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Accommo, Token

# Register your models here.


@admin.register(Accommo, Token)
class ViewAdmin(ImportExportModelAdmin):
    pass
