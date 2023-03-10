"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('SignUp/', views.SignUpUser, name='SignUpUser'),
    path('Logout/', views.LogoutUser, name='LogoutUser'),
    path('Login/', views.LoginUser, name='LoginUser'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.Create, name='Create'),
    path('current/', views.CurrentTodo, name='CurrentTodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
]
