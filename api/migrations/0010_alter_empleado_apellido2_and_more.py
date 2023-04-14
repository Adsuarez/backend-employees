# Generated by Django 4.2 on 2023-04-10 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_appellido2_empleado_apellido2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellido2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='codigo_departamento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.departamento'),
        ),
    ]