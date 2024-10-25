from django.shortcuts import render

#FUNÇÕES AQUI!!
#Renderização: converter aquivo para 100% HTML

def inicial(request):
    return render(request, "index.html")

def contato(request):
    return render(request, "contato.html")

def seila(request):
    return render(request, "seila.html")