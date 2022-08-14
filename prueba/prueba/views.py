from django.shortcuts import render

def index(request):
    return render (request, 'index.html', {
        #context
        'mensaje': 'Este es el contexto o diccionario en django.',
        'prod1': 'Maleta',
        'prod2': 'Audifonos',
        'prod3': 'Celular'
    })

def contacto(request):
    return render (request, 'contacto.html', {

    })