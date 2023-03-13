from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('inicio', inicio, name="AppCoderInicio"),
    path('cursos', cursos, name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
    path('formulario_curso', formulario_curso, name="AppCoderFormularioCurso"),
    path('formulario_estudiante', formulario_estudiante, name="AppCoderFormularioEstudiante"),
    path('formulario_profesor', formulario_profesor, name="AppCoderFormularioProfesor"),
    path('formulario_entregable', formulario_entregable, name="AppCoderFormularioEntregable"),
    path('busqueda', busqueda, name="AppCoderBusquedaCamada"),
    path('buscar/', buscar, name="AppCoderResultadoPorBusqueda"),
]
