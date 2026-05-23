from django.contrib import admin
from django.urls import path
from . import views_simples

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_simples.lista_produtos, name='lista'),
    path('cadastrar/', views_simples.cadastrar, name='cadastrar'),
    path('editar/<int:id>/', views_simples.editar, name='editar'),
    path('excluir/<int:id>/', views_simples.excluir, name='excluir'),
]