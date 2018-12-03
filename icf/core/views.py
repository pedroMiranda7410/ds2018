from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.models import User
from core.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST
import random
import datetime
import time
from core.models import Usuario

### Java values ###
def num_java():

    c = len(Usuario.objects.filter(conhecimento_java=True))
    lista = []
    lista = Usuario.objects.filter(conhecimento_java=True)

    return c
c = num_java()

def nomes_java():
    lista_objts = []
    lista_objts = Usuario.objects.filter(conhecimento_java=True)
    lista_nomes = []
    i = 0
    j = 0
    for i in lista_objts:
        lista_nomes.append(lista_objts[j].nome)
        j = j + 1
        #print(lista_nomes)
        #print(Usuario.objects.all().values('nome'))
    return lista_nomes

nomes_j = nomes_java()

def nomes_teste():
    lista_objts = []
    lista_objts = Usuario.objects.filter(conhecimento_java=True)
   
        #print(lista_nomes)
        #print(Usuario.objects.all().values('nome'))
    return lista_objts[0].nome

nomes_teste = nomes_teste()

###  python values ###
def num_python():
    d = len(Usuario.objects.filter(conhecimento_python=True))
    return d

d = num_python()

def nomes_python():
    lista_objts = []
    lista_objts = Usuario.objects.filter(conhecimento_python=True)
    lista_nomes = []
    i = 0
    j = 0
    for i in lista_objts:
        lista_nomes.append(lista_objts[j].nome)
        j = j + 1
        #print(lista_nomes)
        #print(Usuario.objects.all().values('nome'))
    return lista_nomes

nomes_p = nomes_python();

### aero values ###
def num_aero():
    e = len(Usuario.objects.filter(conhecimento_aeromodelismo=True))
    return e
    
e = num_aero()

def nomes_aero():
    lista_objts = []
    lista_objts = Usuario.objects.filter(conhecimento_aeromodelismo=True)
    lista_nomes = []
    i = 0
    j = 0
    for i in lista_objts:
        lista_nomes.append(lista_objts[j].nome)
        j = j + 1
        #print(lista_nomes)
        #print(Usuario.objects.all().values('nome'))
    return lista_nomes

nomes_a = nomes_aero();

### fenomenos values ###
def num_fenomenos():
    f = len(Usuario.objects.filter(conhecimento_fenomenos=True))
    return f

f = num_fenomenos()

def nomes_fenomenos():
    lista_objts = []
    lista_objts = Usuario.objects.filter(conhecimento_fenomenos=True)
    lista_nomes = []
    i = 0
    j = 0
    for i in lista_objts:
        lista_nomes.append(lista_objts[j].nome)
        j = j + 1
        #print(lista_nomes)
        #print(Usuario.objects.all().values('nome'))
    return lista_nomes

nomes_f = nomes_fenomenos();

### num pessoas ###
def num_pessoas():
    usuarios = Usuario.objects.all().values('id')
    g = 0
    for i in usuarios:
        if True:
            g = g + 1
    return g

g =num_pessoas()

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/index.html', {'filter': user_filter})

def home(request):
    return render(request,'index.html',{'teste': nomes_teste,'numero_java': c,'nomes_java': nomes_j, 'numero_python':d,'nomes_python': nomes_p, 'numero_aero':e,'nomes_aero':nomes_a , 'numero_fenomenos':f,'nomes_fenomenos':nomes_f, 'numero_pessoas':g})

def homeProfessor(request):
    return render(request,'homeProfessor.html',{'numero_java': c,'nomes_java': nomes_j, 'numero_python':d,'nomes_python': nomes_p, 'numero_aero':e,'nomes_aero':nomes_a , 'numero_fenomenos':f,'nomes_fenomenos':nomes_f, 'numero_pessoas':g})

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

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homeProfessor.html'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'forms.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #login(request,user)
                #return HttpResponseRedirect(reverse('index.html'))
                return render(request,'index.html')

            else:

                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'login.html')

    else:
        return render(request, 'login.html', {})

