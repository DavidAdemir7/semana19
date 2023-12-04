from django.db import models
from django.contrib.auth.models import Group

Group.objects.get_or_create(name='cajero')
Group.objects.get_or_create(name='Estudiante')


class Proovedores(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre
    
class Produtos(models.Model):
        nombre = models.CharField(max_length=100)
        stock = models.PositiveBigIntegerField()
        fk_prov = models.ForeignKey(Proovedores,on_delete=models.CASCADE )

        def __str__(self):
             return self.nombre
