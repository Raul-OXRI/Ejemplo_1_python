from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad,cursoC,cursoCss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', dameFecha),
    path('edades/<int:edad>/<int:agno>', calculaEdad),
    path('cursoC/', cursoC),
    path('cursoCss/', cursoCss),
]