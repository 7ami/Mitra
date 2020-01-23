from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Accommo, Token, Tour, Guide

# Register your models here.


@admin.register(Accommo, Token, Tour, Guide)
class ViewAdmin(ImportExportModelAdmin):
    pass
