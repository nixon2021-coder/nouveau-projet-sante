import email
from email import message
from email.message import Message
from unicodedata import name
from django.shortcuts import render, redirect
from service.models import *
from medecine.models import *
from django.contrib import messages
import re

def index(request):
    banner = Banner.objects.all()
    equipe = Team.objects.all()

    form = ""
    if request.method == "POST" :

        name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Message = request.POST.get('message')

       
        Contact.objects.create(
            nom=name,
            email=Email,
            telefone=Phone,
            message=Message, )

        form = messages.add_message(request, messages.SUCCESS, 'Votre dossier a bien été soumis.')
        return redirect('index')
    #return redirect('messages.html',)
    return render(request, 'index.html',locals())
    

    #else:
         #email = request.POST["email"]
         #regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

         #if re.match(regex, email):
           
             #return redirect("index")

    


    




