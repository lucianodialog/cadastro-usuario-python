from django.urls import path
from  . import views 

urlpatterns = [
    path('usuarios/', views.cadastroUsuario),
    path('novoUsuario/', views.novoUsuario, name="novo-usuario"),
    path('listar_usuarios/', views.listarUsuarios, name="listar-usuarios"),
]