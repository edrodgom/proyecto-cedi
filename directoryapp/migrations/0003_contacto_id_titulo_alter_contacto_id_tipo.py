# Generated by Django 4.1.6 on 2023-02-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryapp', '0002_alter_contacto_id_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='id_titulo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id_tipo',
            field=models.IntegerField(),
        ),
    ]