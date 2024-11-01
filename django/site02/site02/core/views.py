from django.shortcuts import render

def nome(request):
    context = {
        "meu_nome":"Analu",
        "idade": 17,
        "curso": "informática" 
    }
    return render(request, 'nome.html', context)

def cadastro(request, nome, idade, curso):
    context = {
        "nome_url": nome,
        "idade_url": idade,
        "curso_url": curso,
    }
    return render(request, 'cadastro.html', context)

def soma(request, n1, n2):
    summ = {
        "r" : n1+n2,
    }
    return render(request, 'soma.html', summ)

def multiplicacao(request, n3, n4):
    mult = {
        "a" : n3*n4,
    }
    return render(request, 'multiplicacao.html', mult)

def divisao(request, n5, n6):
    div = {
        "b" : n5/n6,
    }
    return render(request, 'divisao.html', div)

def subtracao(request, n7, n8):
    sub = {
        "c" : n7-n8,
    }
    return render(request, 'subtracao.html', sub)

