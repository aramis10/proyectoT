from django.db import models

# Create your models here.
class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    date = models.CharField(max_length=50,blank=True)
    club = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto de la persona')
    )

class Meta:
    verbose_name = ('Persona')
    verbose_name_plural = ('Personas')

def __str__(self):
    return self.nombre
