from django.shortcuts import render
from AppCoder.models import Curso, Inicio, Entregable, Estudiante, Profesor
from AppCoder.forms import Formulario_curso, Formulario_entregable, Formulario_estudiante, Formulario_profesor

def inicio(request):
    inicio_template = Inicio.logo
    context = {
        "inicio": inicio_template
    }
    return render(request, "AppCoder/inicio.html", context=context)


def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/cursos.html", context=context)


def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)


def estudiantes(request):
    return render(request, "base.html")


def profesores(request):
    return render(request, "base.html")


def formulario_curso(request):
    if request.method == 'POST':
        mi_formulario = Formulario_curso(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = Formulario_curso()
    return render(request, "AppCoder/formulario_curso.html", {"mi_formulario": mi_formulario})


def formulario_entregable(request):
    if request.method == 'POST':
        mi_formulario = Formulario_entregable(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                    curso=informacion['curso'], camada=informacion['camada'],
                                    fecha_de_entrega=informacion['fecha_de_entrega'], entregado=informacion['entregado'])
            entregable.save()
            return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = Formulario_entregable()
    return render(request, "AppCoder/formulario_entregable.html", {"mi_formulario": mi_formulario})


def formulario_estudiante(request):
    if request.method == 'POST':
        mi_formulario = Formulario_estudiante(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                    email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = Formulario_estudiante()
    return render(request, "AppCoder/formulario_estudiante.html", {"mi_formulario": mi_formulario})


def formulario_profesor(request):
    if request.method == 'POST':
        mi_formulario = Formulario_profesor(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = Formulario_profesor()
    return render(request, "AppCoder/formulario_profesor.html", {"mi_formulario": mi_formulario})
