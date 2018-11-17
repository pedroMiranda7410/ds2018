from django.contrib import admin
from django.urls import path, include
from core.views import home
from core.views import charts
from core.views import forms
from core.views import login
from core.views import registro
from core.views import tabelas
from core.views import update
from django.conf.urls import url
from core.views import alterarSenha
from core.views import user_login
from core.views import register
from core import views

# SET THE NAMESPACE!
app_name = 'core'

urlpatterns = [
    #url(r'^$', views.index, name ='index'),
    url(r'^$', forms, name="forms"),
    #path("forms/", forms, name = "forms"),
    url(r'^$', update, name="update"),
    url(r'^register/$',register,name='register'),
    url(r'^user_login/$',user_login,name='user_login'),
]
