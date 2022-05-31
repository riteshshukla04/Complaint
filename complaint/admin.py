from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class ComplaintAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Complaint,ComplaintAdmin)
# Register your models here.
