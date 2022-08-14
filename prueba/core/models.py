from tabnanny import verbose
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marca'
        ordering = ['id']



class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

