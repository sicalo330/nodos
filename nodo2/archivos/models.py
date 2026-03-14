from django.db import models

class fragmentoArchivo(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    nodo = models.CharField(max_length=50)
    fragmento = models.CharField(max_length=50)
    ruta = models.TextField()

    def __str__(self):
        return f"{self.nombre_archivo} - {self.nodo}"