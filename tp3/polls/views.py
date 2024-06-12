from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import *
import matplotlib.pyplot as plt
import io
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings 
from django.db.models import Avg,Sum,Min,Max
# Create your views here.

def home(request):
    Patient_data=Patient.objects.all()
    return render(request, 'tp3/home.html',{'Patient':Patient_data})

def data_set(request):
    return render(request, 'tp3/data_set.html')

def consulta(request):
    file = open('static/CVD_cleaned.csv')
    datos = csv.DictReader(file)
    for fila in datos:
        Patient.objects.create(
            general_health = fila[0],
            checkup = fila[1],
            exercise = fila[2],
            heart_disease = fila[3],
            skin_cancer = fila[4],
            other_cancer = fila[5],
            depression = fila[6],
            diabetes = fila[7],
            arthritis = fila[8],
            sex = fila[9],
            age_category = fila[10],
            height = fila[11],
            weight = fila[12],
            bmi = fila[13],
            smoking_history = fila[14],
            alcohol_consumption = fila[15],
            fruit_consumption = fila[16],
            green_vegetables_consumption = fila[17],
            fried_potato_consumption = fila[18],

            
        )
    return HttpResponse(request('Archivo cargado'))

def show_graph(request):
    # Obtener datos de los pacientes
    patients = Patient.objects.all()
    General_Health = [patient.general_health for patient in patients]
    Heart_Deseases = [patient.heart_disease for patient in patients]

    # Crear la figura y el gráfico
    plt.figure(figsize=(10,6))
    plt.plot(General_Health,Heart_Deseases)
    plt.xlabel('general_health')
    plt.ylabel('heart_disease')
    plt.title('Salud de los Pacientes')
    plt.show()

    # Guardar la figura en un archivo temporal
    graph_dir = os.path.join(settings.BASE_DIR, 'static', 'img')
    os.makedirs(graph_dir, exist_ok=True)  # Crear el directorio si no existe
    graph_path = os.path.join(graph_dir, 'patient_heart_rates.png')

    # Guardar la figura en el archivo
    plt.savefig(graph_path)
    

    # Pasar la URL del archivo a la plantilla
    graph_url = os.path.join(settings.STATIC_URL, 'img', 'patient_heart_rates.png')

    return render(request, 'tp3/home.html', {'graph_url': graph_url})

