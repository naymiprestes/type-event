from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def new_event(request):
    if request.method == "GET":
        return render(request, 'new_event.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')


        evento = Event(
            criador=request.user,
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horaria=carga_horaria,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo,
            logo=logo,
        )

        evento.save()

        messages.add_message(request, constants.SUCCESS, "Evento cadastrado com sucesso.")
        return redirect(reverse("new_event"))
    


def manage_event(request):
    if request.method == "GET":
        events = Event.objects.filter(criador = request.user)
        return render(request, "manage_event.html", {"events": events})