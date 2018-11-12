from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def homeProfessor(request):
    return render(request,'homeProfessor.html')

def charts(request):
    return render(request,'charts.html')

def forms(request):
    return render(request,'forms.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'register.html')

def tabelas(request):
    return render(request,'tables.html')

def cadastroSucesso(request):
    return render(request,'cadastroSucesso.html')

def esqueceuSenha(request):
    return render(request,'esqueceuSenha.html')

def update(request):
    return render(request,'update.html')

def alterarSenha(request):
    return render(request,'alterarSenha.html')

def senhaAlterada(request):
    return render(request,'senhaAlterada.html')
