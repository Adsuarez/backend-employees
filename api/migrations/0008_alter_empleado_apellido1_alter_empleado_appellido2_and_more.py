# Generated by Django 4.2 on 2023-04-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_departamento_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellido1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='appellido2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nif',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]