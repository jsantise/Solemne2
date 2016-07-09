
from django.shortcuts import render

from catalogo.models import Categoria, Producto, Marca



def view_index(request):
	pass

def index(request):

	categorias = Categoria.objects
	return render(request, 'index.html', {'categorias':categorias})