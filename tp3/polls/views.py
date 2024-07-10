from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import *
import matplotlib.pyplot as plt
from django.urls import reverse
import pandas as pd




def home(request):
    return render(request, 'tp3/home.html',{'Patient':Patient})
    

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


def tabla_datos(request):
    Patient_data=Patient.objects.all()
    return render(request, 'tp3/tabla_datos.html', {'Patient': Patient_data})


from django.shortcuts import render

# Datos de ejemplo para la lógica de predicción mejorada
RISK_FACTORS = {
    'age': 60,
    'cholesterol': 'Yes',
    'smoking': 'Yes',
    'general_health': ['poor', 'fair'],
    'exercise': 'No'
}

def evaluar_problema_corazon(age, cholesterol, smoking, general_health, exercise):
    # Definir criterios de riesgo basados en el análisis de datos
    age_risk = age >= RISK_FACTORS['age']
    cholesterol_risk = cholesterol == RISK_FACTORS['cholesterol']
    smoking_risk = smoking == RISK_FACTORS['smoking']
    general_health_risk = general_health in RISK_FACTORS['general_health']
    exercise_risk = exercise == RISK_FACTORS['exercise']
    
    # Calcular el riesgo total
    risk_score = sum([age_risk, cholesterol_risk, smoking_risk, general_health_risk, exercise_risk])
    
    # Definir umbral de riesgo
    if risk_score >= 3:
        return "Propenso a tener problemas de corazón"
    else:
        return "No es propenso a tener problemas de corazón"

def evaluar_html(request):
    resultado = None
    if request.method == 'POST':
        age = int(request.POST.get('age', 0))
        cholesterol = request.POST.get('cholesterol', 'No')
        smoking = request.POST.get('smoking', 'No')
        general_health = request.POST.get('general_health', 'good')
        exercise = request.POST.get('exercise', 'Yes')

        resultado = evaluar_problema_corazon(age, cholesterol, smoking, general_health, exercise)
    
    return render(request, 'tp3/formulario.html', {'resultado': resultado})
