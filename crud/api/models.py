from django.db import models

class Departamento(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.BigIntegerField()

    def __str__(self):
        return f"{self.codigo}"
    
    
    
class Empleado(models.Model):
    codigo = models.SmallIntegerField(primary_key=True)
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100, default="")
    codigo_departamento = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo}"
