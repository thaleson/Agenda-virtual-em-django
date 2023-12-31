from django.db import models
from django.utils import timezone

""" 
CONTATOS
id: INT (automático)
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

 CATEGORIA
 id: INT
 nome: STR * (obrigatório)"""


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) :
        return self.nome


class  Contato(models.Model):

    nome=models.CharField(max_length=255)
    sobrenome=models.CharField(max_length=255,blank=True)
    telefone=models.CharField(max_length=255)
    email=models.CharField(max_length=255,blank=True)
    data_criaçao=models.DateTimeField(default=timezone.now)
    descriçao=models.TextField(blank=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    mostrar=models.BooleanField(default=True)
    foto=models.ImageField(blank=True,upload_to='fotos/%Y/%m/%d')


    def __str__(self) :
        return self.nome
     
