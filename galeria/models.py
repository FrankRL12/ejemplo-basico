from django.db import models

# Create your models here.
class Galeria(models.Model):
    imagen = models.ImageField(upload_to='motosicleta')
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    precio = models.IntegerField()
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='galeria'
        verbose_name_plural='galerias'

    def __str__(self):
        return self.titulo