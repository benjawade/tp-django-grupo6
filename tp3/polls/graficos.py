from models import Patient
import matplotlib.pyplot as plt
import numpy as np


# Definir un diccionario con palabras y sus valores correspondientes

hombres_sanos=Patient.objects.get(general_health='Very Good',)

