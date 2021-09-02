from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.inicio),
    #CRUD
    path('registrar', views.registrar), #crear
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    path('eliminar', views.eliminar),
]