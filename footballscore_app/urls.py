"""footballscore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from footballscore_app import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='index'),
    path('league/', views.LeagueView.as_view(), name="league"),
    path('add_league/', views.AddLeagueView.as_view(), name="add_league"),
    path('edit_league/<int:pk>/', views.EditLeagueView.as_view(), name="edit_league"),
    path('delete_league/<int:pk>/', views.DeleteLeagueView.as_view(), name="delete_league"),

]

