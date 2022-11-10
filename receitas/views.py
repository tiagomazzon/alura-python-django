from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Receita


def index(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    else:
        receitas = ''

    dados = {
        'receitas' : receitas
    }
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request,'receita.html', receita_a_exibir)

def resultados(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'resultados.html', dados)