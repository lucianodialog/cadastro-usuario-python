from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
def cadastroUsuario(request):
    return render(request, 'usuarios/cadastro_usuarios.html')

def novoUsuario(request):
    usuario = Usuario()
    if request.method == 'POST':
        print("chegou aqui")
        
        usuario.nome = request.POST.get('nome', None)
        usuario.senha = request.POST.get('senha', None)
        usuario.email = request.POST.get('email', None)
        usuario.endereco = request.POST.get('endereco', None)
        usuario.telefone = request.POST.get('telefone', None)         
        usuario.save()    
    
        
    return render(request, 'usuarios/cadastro_usuarios.html')

def listarUsuarios(request):
    lista_usuarios = Usuario.objects.all()
    print(lista_usuarios)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': lista_usuarios})