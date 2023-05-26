from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    
# PASOS:
# 1.- preparar la migración
# py manage.py makemigrations crud
# 2.- ejecutar la migración
# py manage.py migrate


### otras clases que representan los modelos