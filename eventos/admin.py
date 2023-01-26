from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Usuario,UserAdmin)
admin.site.register(Participante)
admin.site.register(Responsable)
admin.site.register(Instructor)
admin.site.register(Evento)