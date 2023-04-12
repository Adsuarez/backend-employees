from django.urls import path
from . import views

urlpatterns = [
    path('departamentos/', views.getAllDepartments),
    path('departamentos/crear/', views.createDepartment),
    path('empleados/', views.getAllEmployees),
    path('empleados/<int:code>/', views.getEmployee),
    path('empleados/crear/', views.createEmployee),
    path('empleados/actualizar/<int:code>/', views.updateEmployee),
    path('empleados/eliminar/<int:code>/', views.deleteEmployee),
]
