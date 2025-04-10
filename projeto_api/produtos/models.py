from django.db import models

class Categoria (models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Produto (models.Model):
    nome= models.CharField(max_lenght=100)
    descricao= models.TetxtField()
    preco= models.DecimalField(max_digits= 10, decimal_places= 2)
    categoria= models.ForeignKey(Categoria, related_name='produtos', on_delete= models.CASCADE)

    def __str__(self):
        return self.nome
# Create your models here.
