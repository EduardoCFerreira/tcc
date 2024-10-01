from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=65)

    def __str__ (self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__ (self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=600)
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='bibliotech/covers/%Y/%m/%d/')
    quantidade = models.PositiveIntegerField(default=1)
    emprestado = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True
    )

    def __str__ (self):
        return self.title
    
class Emprestimo(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    data_retirada = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    observacao = models.CharField(max_length=300)
    emprestado = models.BooleanField(default=False)

    def __str__ (self):
        return self.observacao