import matplotlib.pyplot as plt
from django.db import models
from Patient.models import Patient

Hombres_sanos=Patient.objects.get(general_health='Very Good')