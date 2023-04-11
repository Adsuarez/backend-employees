from django.urls import path
from . import views

urlpatterns = [
    path('departamentos/', views.getAllDepartments),
    path('departamentos/crear', views.createDepartment),
    path('empleados/', views.getAllEmployees),
    path('empleados/crear', views.createEmployee),
    path('empleados/actualizar', views.updateEmployee),
]
