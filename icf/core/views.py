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

def num_java():
    usuarios = Usuario.objects.all().values('conhecimento_java')
    c =0
    i=0
    for i in usuarios:
        if  True:
            c = c + 1
    return c  

c = num_java()    

def num_python():
    usuarios = Usuario.objects.all().values('conhecimento_python')
    d = 0
    i=0
    for i in usuarios:
        if True:
            d = d + 1
    return d

d = num_python()

def num_aero():
    usuarios = Usuario.objects.all().values('conhecimento_aeromodelismo')
    e = 0
    i=0
    for i in usuarios:
        if True:
            e = e + 1
    return e
    
e = num_aero()

def num_fenomenos():
    usuarios = Usuario.objects.all().values('conhecimento_fenomenos')
    f = 0
    i=0
    for i in usuarios:
        if True:
            f = f + 1
    return f

f = num_fenomenos()

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
    return render(request,'index.html')

def homeProfessor(request):
    return render(request,'homeProfessor.html',{'numero_java': c, 'numero_python':d, 'numero_aero':e , 'numero_fenomenos':f, 'numero_pessoas':g})

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

