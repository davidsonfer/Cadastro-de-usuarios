from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referência
    path('', views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('deletar_usuario/<int:id>/', views.deletar_usuario, name="deletar_usuario")
]