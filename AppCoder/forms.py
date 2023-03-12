from django import forms


class Formulario_curso(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class Formulario_estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class Formulario_profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class Formulario_entregable(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    curso = forms.CharField()
    camada = forms.IntegerField()
    fecha_de_entrega = forms.DateField(input_formats=['%d/%m/%Y'])
    entregado = forms.BooleanField()


