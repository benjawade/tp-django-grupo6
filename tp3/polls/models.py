from django.db import models

# Create your models here.

class PatientData(models.Model):
    general_health = models.CharField(max_length=100)
    checkup = models.CharField(max_length=100)
    exercise = models.CharField(max_length=100)
    heart_disease = models.CharField(max_length=100)
    skin_cancer = models.CharField(max_length=100)
    other_cancer = models.CharField(max_length=100)
    depression = models.CharField(max_length=100)
    diabetes = models.CharField(max_length=100)
    arthritis = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age_category=models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    smoking_history = models.CharField(max_length=100)
    alcohol_consumption = models.FloatField()
    fruit_consumption = models.FloatField()
    green_vegetables_consumption = models.FloatField()
    fried_potato_consumption = models.FloatField()

