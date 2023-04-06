from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mensaje=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

