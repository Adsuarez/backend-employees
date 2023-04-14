from rest_framework.serializers import ModelSerializer
from .models import Empleado, Departamento

class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
