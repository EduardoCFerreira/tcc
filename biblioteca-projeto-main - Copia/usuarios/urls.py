from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('emprestimo/', views.emprestimo, name='emprestimo'),
    path('livro-editar-detalhe/', views.livro_editar_detalhe, name='livro_editar_detalhe'),
    path('livro-editar/<int:id>/', views.livro_editar, name='livro_editar'),
    path('livro-adicionar-detalhe/', views.livro_adicionar_detalhe, name='livro_adicionar_detalhe'),
    path('livro-adicionar/', views.livro_adicionar, name='livro-adicionar'),
]
