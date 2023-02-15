# Generated by Django 4.1.6 on 2023-02-10 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directoryapp', '0007_cat_cargo_cat_organismo_cat_tipo_empleado_cat_titulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tx_contrasena',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id_usuario_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directoryapp.usuario'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id_usuario_upd',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hist_contacto',
            name='id_usuario_ingreso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='directoryapp.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tx_usuario',
            field=models.CharField(max_length=25),
        ),
    ]
