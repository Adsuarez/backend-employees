# Generated by Django 4.2 on 2023-04-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_empleado_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='codigo',
            field=models.SmallIntegerField(primary_key=True, serialize=False),
        ),
    ]