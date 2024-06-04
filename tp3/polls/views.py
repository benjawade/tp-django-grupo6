from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import PatientData

# Create your views here.

def index(request):
    return HttpResponse('hola')

def consulta(request):
    file = open('static/CVD_cleaned.csv')
    datos = csv.DictReader(file)
    for fila in datos:
        PatientData.objects.create(
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
