from django.http import HttpResponse
from django.template import loader
from indice.models import familiar
import sqlite3

# Create your views here.

def inicio(request):
    return HttpResponse("Hola soy la nueva pagina")


def plantilla(self):

    template=loader.get_template("indice.html")


    familiar=familiar(nombre="", apellido="",dni=0)


    lista=[familiar]
    
    diccionario_de_datos={
        'lista': lista
    }

    # context= Context(diccionario_de_datos)
    plantilla_preparada=template.render(diccionario_de_datos) #antes le pasa el context
    return HttpResponse(plantilla_preparada)