from django.contrib import admin
from django.urls import path, include
from core.views import home
from core.views import charts
from core.views import forms
from core.views import login
from core.views import registro
from core.views import tabelas
from django.conf.urls import url


urlpatterns = [
    #url(r'^$', views.index, name ='index'),
    url(r'^$', forms, name="forms"),
    #path("forms/", forms, name = "forms"),
]
