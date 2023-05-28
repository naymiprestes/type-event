from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth


def register (request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

    if not (senha == confirmar_senha):   
        messages.add_message(request, constants.ERROR, "a senha não corresponde")       
        return redirect(reverse('register'))
    
            
    user = User.objects.filter(username=username)

    if user.exists():
            messages.add_message(request, constants.ERROR, "usuário já existe")
            return redirect(reverse('register'))   
            
    user = User.objects.create_user(username=username, email=email, password=senha)
    messages.add_message(request, constants.SUCCESS, "usuário salvo com sucesso")
    user.save()
    return redirect(reverse('login'))



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'username ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/events/new_event/')