
from django.contrib import admin
from catalogo.models import Categoria, Producto, Marca


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order','created_at','updated_at')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name','sku','price','category','created_at','updated_at',)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at',)    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)