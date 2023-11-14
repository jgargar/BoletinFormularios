from django.shortcuts import render
from forms.forms import formularioUnoForms, formularioDosForms, formularioTresForms


# Create your views here.
def index(request):
    return render(request, 'forms/index.html', {})


def formulario_uno(request):
    formulario = formularioUnoForms()
    # Si se ha enviado el formulario
    if request.method == "POST":
        formulario = formularioUnoForms(request.POST)
        # Ejecutamos la validacion
        if formulario.is_valid():
            fecha_inicio = formulario.cleaned_data['fecha_inicio']
            fecha_fin = formulario.cleaned_data['fecha_fin']
            dias_semana = formulario.cleaned_data['dias_semana']
            email = formulario.cleaned_data['email']
            # Instanciamos el objeto tablero
            return render(request, 'forms/index.html', {})  # Le paso por el contexto el tablero del objeto tablero
    # Si se se pide la pagina por primera vez
    return render(request, 'forms/formulario.html', {'form': formulario})


def formulario_dos(request):
    formulario = formularioDosForms()
    # Si se ha enviado el formulario
    if request.method == "POST":
        formulario = formularioDosForms(request.POST)
        # Ejecutamos la validacion
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            fecha_creacion = formulario.cleaned_data['fecha_creacion']
            # Instanciamos el objeto tablero
            return render(request, 'forms/index.html', {})  # Le paso por el contexto el tablero del objeto tablero
    # Si se se pide la pagina por primera vez
    return render(request, 'forms/formulario.html', {'form': formulario})


def formulario_tres(request):
    if request.method == "POST":
        formulario = formularioTresForms(request.POST, request.FILES)
        if formulario.is_valid():
            imagen = formulario.cleaned_data['imagen']
            with open(f'media/{imagen.name}', 'wb+') as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)
            return render(request, 'forms/index.html', {})
    return render(request, 'forms/formulario.html', {})
