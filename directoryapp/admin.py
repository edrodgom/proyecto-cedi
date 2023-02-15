from django.contrib import admin
from .models import Contacto, Hist_Contacto, Cat_Tipo_Empleado, Cat_Cargo, Cat_Organismo, Cat_Titulo, Cat_Unidad, Usuario

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Hist_Contacto)
admin.site.register(Cat_Tipo_Empleado)
admin.site.register(Cat_Cargo)
admin.site.register(Cat_Organismo)
admin.site.register(Cat_Titulo)
admin.site.register(Cat_Unidad)
admin.site.register(Usuario)