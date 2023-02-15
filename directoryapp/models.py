from django.db import models
from django.utils import timezone

# Create your models here.
class Cat_Tipo_Empleado(models.Model):
    id_tipo_empleado = models.IntegerField(primary_key=True, auto_created=True)
    tx_empleado = models.CharField(max_length=25)
    id_padre_empleado = models.IntegerField()

class Cat_Titulo(models.Model):
    id_titulo = models.IntegerField(primary_key=True, auto_created=True)
    tx_titulo = models.CharField(max_length=30)

class Cat_Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True, auto_created=True)
    tx_cargo = models.CharField(max_length=30)

class Cat_Organismo(models.Model):
    id_organismo = models.IntegerField(primary_key=True, auto_created=True)
    tx_organismo = models.CharField(max_length=25)

class Cat_Unidad(models.Model):
    id_unidad = models.IntegerField(primary_key=True, auto_created=True)
    tx_unidad = models.CharField(max_length=25)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, auto_created=True)
    tx_usuario = models.CharField(max_length=25, blank=False)
    tx_contrasena = models.CharField(max_length=25, null=False, default=None)
    fh_ingreso = models.DateTimeField(blank=False, null=False)
    fh_baja = models.DateTimeField(blank=True, null=True)
    id_tipo_usuario = models.BooleanField("1=Administrador, 2=Operador",default=2)

    def __str__(self):
        return self.id_usuario
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False) 
    a_paterno = models.CharField(max_length=50, null=False) 
    a_materno = models.CharField(max_length=50, null=True) 
    id_tipo_empleado = models.ForeignKey(Cat_Tipo_Empleado, on_delete=models.PROTECT)
    id_titulo = models.ForeignKey(Cat_Titulo, on_delete=models.PROTECT)
    id_cargo = models.ForeignKey(Cat_Cargo, on_delete=models.PROTECT)
    id_organismo = models.ForeignKey(Cat_Organismo, on_delete=models.PROTECT, default=None)
    funcion = models.TextField(null=True)
    id_unidad = models.ForeignKey(Cat_Unidad, on_delete=models.PROTECT)
    tel_ofi = models.CharField(max_length=20, null=True)
    extension = models.CharField(max_length=20, null=True)
    tel_ofi_d = models.CharField(max_length=20, null=True)
    direccion_ext = models.TextField(null=True)
    tel_part_ext = models.CharField(max_length=20, null=True)
    tel_part_d_ext = models.CharField(max_length=20, null=True)
    celular_ext = models.CharField(max_length=20, null=True)
    celular_d_ext = models.CharField(max_length=20, null=True)
    celular_t_ext = models.CharField(max_length=20, null=True)
    celular_c_ext = models.CharField(max_length=20, null=True)
    direccion_mx = models.TextField(null=True)
    tel_part_mx = models.CharField(max_length=20, null=True)
    tel_part_d_mx = models.CharField(max_length=20, null=True)
    celular_mx = models.CharField(max_length=20, null=True)
    celular_d_mx = models.CharField(max_length=20, null=True)
    celular_t_mx = models.CharField(max_length=20, null=True)
    celular_c_mx = models.CharField(max_length=20, null=True)
    observaciones = models.TextField(null=True)
    fh_actualizacion = models.DateTimeField(blank=True, null=True)
    fh_ingreso = models.DateTimeField(default=timezone.now, null=False)
    id_usuario_ingreso = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=False)
    fh_baja = models.DateTimeField(blank=True, null=True)
    id_usuario_upd = models.IntegerField()
    is_active = models.BooleanField(default=1)

class Hist_Contacto(models.Model):
    id_contacto = models.ForeignKey(Contacto, on_delete=models.PROTECT)
    id_tipo = models.IntegerField(null=False)
    id_titulo = models.IntegerField(null=False)
    id_cargo = models.IntegerField(null=False)
    id_organismo = models.IntegerField(null=False)
    funcion = models.TextField(null=True)
    id_unidad = models.IntegerField(null=False)
    id_empleado = models.IntegerField(null=False)
    tel_ofi = models.CharField(max_length=20, null=True)
    extension = models.CharField(max_length=20, null=True)
    tel_ofi_d = models.CharField(max_length=20, null=True)
    direccion_ext = models.TextField(null=True)
    tel_part_ext = models.CharField(max_length=20, null=True)
    tel_part_d_ext = models.CharField(max_length=20, null=True)
    celular_ext = models.CharField(max_length=20, null=True)
    celular_d_ext = models.CharField(max_length=20, null=True)
    celular_t_ext = models.CharField(max_length=20, null=True)
    celular_c_ext = models.CharField(max_length=20, null=True)
    direccion_mx = models.TextField(null=True)
    tel_part_mx = models.CharField(max_length=20, null=True)
    tel_part_d_mx = models.CharField(max_length=20, null=True)
    celular_mx = models.CharField(max_length=20, null=True)
    celular_d_mx = models.CharField(max_length=20, null=True)
    celular_t_mx = models.CharField(max_length=20, null=True)
    celular_c_mx = models.CharField(max_length=20, null=True)
    observaciones = models.TextField(null=True)
    fh_actualizacion = models.DateTimeField(blank=True, null=True)
    fh_ingreso = models.DateTimeField(default=timezone.now, null=False)
    id_usuario_ingreso = models.IntegerField()
    fh_baja = models.DateTimeField(blank=True, null=True)
    id_usuario_upd = models.IntegerField(null=True)
    is_active = models.BooleanField(default=1)





