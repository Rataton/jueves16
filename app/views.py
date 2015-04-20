from django.shortcuts import render
from app.models import Especie, Pato, Secciones
# Create your views here.

def quiero_patos(request):
	patos = Pato.objects.all()
	print request.user
	return render(request,"patos.html",{"patos":patos})

def home(request):
	return render(request, "index.html")