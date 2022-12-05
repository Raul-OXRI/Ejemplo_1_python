from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista
        p1 = Persona("Profesor Juan", "Diaz")
        #nombre = "Juan"
        #apellido = "Diaz"
        #------------------------------------------------------------------------------------------------------
        temasDelCurso=["Plantillas","Modelos","Formulario","Vistas","Despliegue"]
        #------------------------------------------------------------------------------------------------------
        ahora = datetime.datetime.now()
        #------------------------------------------------------------------------------------------------------
        #doc_externo=open("C:/Users/Raul/Documents/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
        #plt= Template(doc_externo.read())
        #doc_externo.close()
        #ctx=Context({"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "momento_actual":ahora, "Temas":temasDelCurso})
        #---------------------------------------------------------------------------------------------------------
        #doc_externo=get_template('miplantilla.html')
        #documento = doc_externo.render({"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "momento_actual":ahora, "Temas":temasDelCurso})
        #-----------------------------------------------------------------------------------------------------
        return render(request, "miplantilla.html", {"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "momento_actual":ahora, "Temas":temasDelCurso})

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoC.html",{"dameFEcha":fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoCss.html",{"dameFEcha":fecha_actual})

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    docummento="<html><body><h2>Fecha y hora actuales %s </h2></body></html>" % fecha_actual
    return HttpResponse(docummento)
    
def calculaEdad(request, edad, agno):
    #edadActual = 18
    periodo = agno-2022
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2></body></html>" % (agno, edadFutura)
    return HttpResponse(documento)