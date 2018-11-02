"""icf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import home
from core.views import charts
from core.views import forms
from core.views import login
from core.views import registro
from core.views import tabelas
from django.conf.urls import url


#urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name ="home"),
    path("forms/", forms, name ="forms"),
    path("charts/", charts, name ="charts"),

    path("login/", login, name ="login"),
    path("registro/", registro, name = "registro"),
    path("tabelas/", tabelas, name = "tabelas"),
]
