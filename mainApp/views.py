from django.shortcuts import render, redirect
from mainApp.forms import UsuarioForm


# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html',{
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainApp/about.html',{
        'title': 'Sobre nosotros'
    })

def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()

    return render(request, 'mainApp/PruebaRegUsu.html',{'form': form})