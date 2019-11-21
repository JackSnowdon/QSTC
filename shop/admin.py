from django.contrib import admin
from .models import Round, RoundTube, Mag, Shader, StockObject, StockReport, Vtip

# Register your models here.


admin.site.register(Round)
admin.site.register(RoundTube)
admin.site.register(Shader)
admin.site.register(Mag)
admin.site.register(Vtip)
admin.site.register(StockReport)
admin.site.register(StockObject)