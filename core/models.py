from django.db import models
from django.utils.timezone import timezone

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return  self.titulo
