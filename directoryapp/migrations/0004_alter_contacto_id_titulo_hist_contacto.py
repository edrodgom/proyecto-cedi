# Generated by Django 4.1.6 on 2023-02-10 04:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('directoryapp', '0003_contacto_id_titulo_alter_contacto_id_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='id_titulo',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Hist_Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo', models.IntegerField()),
                ('id_titulo', models.IntegerField()),
                ('id_cargo', models.IntegerField()),
                ('id_oficina', models.IntegerField()),
                ('funcion', models.TextField(null=True)),
                ('id_unidad', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
                ('tel_ofi', models.CharField(max_length=20, null=True)),
                ('extension', models.CharField(max_length=20, null=True)),
                ('tel_ofi_d', models.CharField(max_length=20, null=True)),
                ('direccion_ext', models.TextField(null=True)),
                ('tel_part_ext', models.CharField(max_length=20, null=True)),
                ('tel_part_d_ext', models.CharField(max_length=20, null=True)),
                ('celular_ext', models.CharField(max_length=20, null=True)),
                ('celular_d_ext', models.CharField(max_length=20, null=True)),
                ('celular_t_ext', models.CharField(max_length=20, null=True)),
                ('celular_c_ext', models.CharField(max_length=20, null=True)),
                ('direccion_mx', models.TextField(null=True)),
                ('tel_part_mx', models.CharField(max_length=20, null=True)),
                ('tel_part_d_mx', models.CharField(max_length=20, null=True)),
                ('celular_mx', models.CharField(max_length=20, null=True)),
                ('celular_d_mx', models.CharField(max_length=20, null=True)),
                ('celular_t_mx', models.CharField(max_length=20, null=True)),
                ('celular_c_mx', models.CharField(max_length=20, null=True)),
                ('observaciones', models.TextField(null=True)),
                ('fh_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('fh_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_usuario_ingreso', models.IntegerField(null=True)),
                ('fh_baja', models.DateTimeField(blank=True, null=True)),
                ('id_usuario_upd', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('id_contacto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directoryapp.contacto')),
            ],
        ),
    ]