"""
URL configuration for spelling_bee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django .views.generic.base import TemplateView

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    path('game_mode', views.game_mode, name="game_mode"),
    path('login', views.login, name="login"),
    path('practice', views.practice, name="practice"),
    path('practice_lists', views.practice_lists, name="practice_lists"),

]

