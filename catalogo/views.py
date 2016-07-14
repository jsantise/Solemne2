
from django.shortcuts import render

from catalogo.models import Categoria, Producto, Marca



def index(request):
    categorias = Categoria.objects.order_by('-name')
    return render(request, 'index.html', {'categorias':categorias})