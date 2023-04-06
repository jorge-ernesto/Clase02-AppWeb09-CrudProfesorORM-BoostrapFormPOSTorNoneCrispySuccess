from django.contrib import admin
from .models import Profesor

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display=['nombre','apellidos','email']
    search_fields=['nombre','apellidos','email']
    list_per_page=10

admin.site.register(Profesor,ProfesorAdmin)