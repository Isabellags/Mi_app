# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta es la ruta por defecto
    
    path('ordenes/', views.listar_ordenes, name='listar_ordenes'),
    path('orden/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('login/', views.login_view, name='login'),
]
