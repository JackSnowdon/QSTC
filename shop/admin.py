from django.contrib import admin
from .models import Round, Mag, Shader

# Register your models here.


admin.site.register(Round)
admin.site.register(Shader)
admin.site.register(Mag)