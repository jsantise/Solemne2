
from django.shortcuts import render

from catalogo.models import Categoria, Producto, Marca



def index(request):
    categorias = Categoria.objects.order_by('-name')
    productos = Producto.objects.order_by('-name')[:3]
    return render(request, 'index.html', {'categorias':categorias, 'productos':productos})

def single(request,sku):
    categorias = Categoria.objects.order_by('-name')
    products = Producto.objects.get(sku=sku)
    return render(request, 'single.html', {'categorias':categorias,'producto':products})

def categoria(request,id):
    categorias = Categoria.objects.order_by('-name')
    productos = Producto.objects.filter(category_id=id)

    return render(request, 'categoria.html', {'productos':productos,'categorias':categorias })