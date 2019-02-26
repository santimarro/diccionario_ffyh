from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404


def index(request):
	return redirect('/search')

def sobre(request):
    return render(request, 'sobre_el_diccionario.html')
