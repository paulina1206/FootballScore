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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BaseView.as_view(), name='index'),
    path('league/', views.LeagueView.as_view(), name="league"),
    path('search_league/', views.SearchLeagueView.as_view(), name="search_league"),
    path('add_league/', views.AddLeagueView.as_view(), name="add_league"),
    path('edit_league/<int:pk>/', views.EditLeagueView.as_view(), name="edit_league"),
    path('delete_league/<int:pk>/', views.DeleteLeagueView.as_view(), name="delete_league"),
    path('detail_league/<int:id>/', views.DetailLeagueView.as_view(), name='detail_league'),
    path('teams/', views.TeamView.as_view(), name="teams"),
    path('search_teams/', views.SearchTeamsView.as_view(), name="search_teams"),
    path('add_team/', views.AddTeamView.as_view(), name="add_team"),
    path('edit_team/<int:id>/', views.EditTeamView.as_view(), name="edit_team"),
    path('delete_team/<int:pk>/', views.DeleteTeamView.as_view(), name="delete_team"),
    path('detail_team/<int:id>/', views.DetailTeamView.as_view(), name='detail_team'),
    path('add_match/', views.AddMatchView.as_view(), name="add_match"),
    path('search_match/', views.SearchMatchView.as_view(), name="search_match"),
    path('delete_match/<int:pk>/', views.DeleteMatchView.as_view(), name="delete_match"),
    path('edit_match/<int:pk>/', views.EditMatchView.as_view(), name="edit_match"),
    path('add_season/', views.AddSeasonView.as_view(), name="add_season"),
    path('edit_season/<int:pk>/', views.EditSeasonView.as_view(), name="edit_season"),
    path('delete_season/<int:pk>/', views.DeleteSeasonView.as_view(), name="delete_season"),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


