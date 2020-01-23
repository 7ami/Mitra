from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Accommo, Token, Tour ,Taxi

# Register your models here.


@admin.register(Accommo, Token, Tour,Taxi)
class ViewAdmin(ImportExportModelAdmin):
    pass
