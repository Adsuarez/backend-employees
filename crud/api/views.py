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

    if not(('codigo' in dataList) & ('nif' in dataList) & ('nombre' in dataList) & ('apellido1' in dataList)):
        return Response("bad or missing register information", status=400)
    
    if not 'apellido2' in dataList:
        data['apellido2'] = ""
    
    #verify if department exist with code
    check_result = list(Departamento.objects.all())
    print("\n before: \n")
    if (not data['codigo_departamento'] in check_result):
        print(f"\n the array check_result is: {check_result[0]} \n")
    print("^ after \n")

    if (not 'codigo_departamento' in dataList) | (not data['codigo_departamento'] in check_result):
        instanced_codigo_departamento = None
    else:
        instanced_codigo_departamento = Departamento.objects.get(codigo = data['codigo_departamento'])      

    try:
        empleado = Empleado.objects.create(
            codigo = data['codigo'],
            nif = data['nif'],
            nombre = data['nombre'],
            apellido1 = data['apellido1'],
            apellido2 = data['apellido2'],
            codigo_departamento = instanced_codigo_departamento
        )
    except Exception as e:
        print(f"\n ----> FROM CREATE VALUE OF ERROR IS: {e.args} \n")
        return Response(e.args, status=409)
    
    try:
        serializers = EmpleadoSerializer(empleado, many=False)
        return Response(serializers.data, status=201)
    except Exception as e:
        print(f"\n ----> FROM SERIALIZED VALUE OF ERROR IS: {e.args} \n")
        return Response(e.args, status=401)
    
@api_view(['POST'])
def createDepartment(request):
    data = request.data
    try:
        departamento = Departamento.objects.create(
            codigo = data['codigo'],
            nombre = data['nombre'],
            presupuesto = data['presupuesto']
        )
        serializers = DepartamentoSerializer(departamento, many=False)
        return Response(serializers.data, status=201)
    except ValueError:
        raise Response(ValueError)