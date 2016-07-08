
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    banner = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
    sort_order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/data',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Producto(models.Model):
    sku = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    marca = models.ForeignKey(Marca)
    category = models.ForeignKey(Categoria)
    image = models.ImageField(upload_to='images/data',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


