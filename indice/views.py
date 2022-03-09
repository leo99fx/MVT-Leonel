from django.http import HttpResponse
import random
from datetime import datetime
from django.template import Context, Template, loader
from indice.models import familiar

# Create your views here.

def inicio(request):
    return HttpResponse("Hola soy la nueva pagina")


def plantilla(self):

    template=loader.get_template("indice.html")


    familiar1=familiar(nombre="Leonel", apellido="Fernandes",dni="41799417")

    lista=[familiar1]
    
    diccionario_de_datos={
        'lista': lista
    }

    # context= Context(diccionario_de_datos)
    plantilla_preparada=template.render(diccionario_de_datos) #antes le pasa el context
    return HttpResponse(plantilla_preparada)