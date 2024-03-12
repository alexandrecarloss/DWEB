from django.db import models

class petteste(models.Model):
    #petid: models.IntegerField()
    nome = models.CharField(max_length=100)
    #foto: models.ImageField(upload_to='adocao/img')

    def __str__(self):
        return self.nome

