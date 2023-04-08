from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.getAllEmployees),
    path('departamentos/', views.getAllDepartments),
    path('empleado/', views.createEmployee),
]
