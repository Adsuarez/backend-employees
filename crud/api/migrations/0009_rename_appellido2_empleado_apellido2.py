# Generated by Django 4.2 on 2023-04-08 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_empleado_apellido1_alter_empleado_appellido2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='appellido2',
            new_name='apellido2',
        ),
    ]
