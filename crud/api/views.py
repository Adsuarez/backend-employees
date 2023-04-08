from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Empleado, Departamento
from api.serializers import EmpleadoSerializer, DepartamentoSerializer

@api_view(['GET'])
def getAllEmployees(request):
    empleado = Empleado.objects.all()
    serializers = EmpleadoSerializer(empleado, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getAllDepartments(request):
    departamento = Departamento.objects.all()
    serializers = DepartamentoSerializer(departamento, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def createEmployee(request):
    data = request.data
    empleado = Empleado.objects.create(
        codigo = data['codigo'],
        nif = data['nif'],
        nombre = data['nombre'],
        apellido1 = data['apellido1'],
        apellido2 = data['apellido2']
    )
    serializers = EmpleadoSerializer(empleado, many=False)
    return Response(serializers.data)
        