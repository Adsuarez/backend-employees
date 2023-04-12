from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Empleado, Departamento
from api.serializers import EmpleadoSerializer, DepartamentoSerializer

LENGTH_EMPLOYEE_MODEL = 4

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
    except Exception as e:
        raise Response(e.args, status=400)
    
@api_view(['GET'])
def getAllDepartments(request):
    departamento = Departamento.objects.all()
    serializers = DepartamentoSerializer(departamento, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getAllEmployees(request):
    empleado = Empleado.objects.all()
    serializers = EmpleadoSerializer(empleado, many=True)
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
    
    #verify if passed code of department already exists
    departments = Departamento.objects.all()
    departments_dirty_list = list(departments)
    departments_list = []
    
    for department in departments_dirty_list:
       departments_list.append(department.codigo)

    if not 'codigo_departamento' in dataList:
        instanced_codigo_departamento = None
    elif not data['codigo_departamento'] in departments_list:
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
        return Response(e.args, status=409)
    
    try:
        serializers = EmpleadoSerializer(empleado, many = False)
        return Response(serializers.data, status=201)
    except Exception as e:
        return Response(e.args, status=401)
    
@api_view(['PUT'])
def updateEmployee(request, code):
    data = request.data
    
    if not is_code_valid(code):
        return Response("user not found", status=404)
    
    empleado = Empleado.objects.get(codigo = code)
    serializers = EmpleadoSerializer(instance = empleado, data = data)
    if not serializers.is_valid():
        return Response("bad or missing updating information", status=400)
    serializers.save()
    return Response(serializers.data, status=202)

@api_view(['DELETE'])
def deleteEmployee(request, code):
    
    if not is_code_valid(code):
        return Response("user not found", status=404)
    
    empleado = Empleado.objects.get(codigo = code)
    empleado.delete()
    return Response("user deleted successfully", status=204)

def is_code_valid(code):
    employees = Empleado.objects.all()
    employees_dirty_list = list(employees)
    employees_list = []

    for employee in employees_dirty_list:
        employees_list.append(employee.codigo)

    if not code in employees_list:
        return False
    
    return True