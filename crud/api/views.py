from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Empleado, Departamento
from api.serializers import EmpleadoSerializer, DepartamentoSerializer

LENGTH_EMPLOYEE_MODEL = 4

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
    
    if len(data) < LENGTH_EMPLOYEE_MODEL:
        return Response("bad or missing register information", status=400)
    
    dataList = list(data)
    if not 'apellido2' in dataList:
        data['apellido2'] = ""

    if not 'codigo_departamento' in dataList:
        data['codigo_departamento'] = None

    print(f"codigo departamento enviado es: {data['codigo_departamento']}")

    try:
        empleado = Empleado.objects.create(
            codigo = data['codigo'],
            nif = data['nif'],
            nombre = data['nombre'],
            apellido1 = data['apellido1'],
            apellido2 = data['apellido2'],
            codigo_departamento = data['codigo_departamento']
        )
        serializers = EmpleadoSerializer(empleado, many=False)
        return Response(serializers.data)
    except:
        return Response("employee already exist", status=409)