from django.db import models

class Usuarios(models.Model):
    nomes= models.CharField(max_length=50)
    bandas = models.CharField(max_length=50)
    filmes = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nomes 
    
