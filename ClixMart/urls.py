"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from myapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.login, name='login'),
    path('index.html', v.index, name='index'),
    path('login.html', v.login, name='login'),
    path('accounts.html', v.accounts, name='accounts'),
    path('add_brand.html', v.add_brand, name='add_brand'),
    path('add_item.html', v.add_item, name='add_item'),
    path('add_cat.html', v.add_cat, name='add_cat'),
    path('change_pass.html', v.change_pass, name='change_pass'),
]