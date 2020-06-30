from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from footballscore_app.forms import LeagueForm, TeamForm, MatchForm
from footballscore_app.models import Match, League, Team
from datetime import date


# Create your views here.
class BaseView(View):
    def get(self, request):
        matches = Match.objects.filter(date=date.today())
        leagues = League.objects.all()
        return render(request, "index.html", {'matches': matches, 'leagues': leagues})



class LeagueView(View):
    def get(self, request):
        leagues = League.objects.all()
        return render(request, "league.html", {'objects': leagues})


class AddLeagueView(PermissionRequiredMixin, CreateView):
    permission_required = 'footballscore_app.add_league'
    form_class = LeagueForm
    template_name = 'add_league.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': League.objects.all()})
        return context


class EditLeagueView(UpdateView):
    model = League
    fields = ['name', 'description', 'hierarchy', 'country']
    template_name = 'edit_league.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': League.objects.all()})
        return context


class DeleteLeagueView(DeleteView):
    model = League
    template_name = 'delete_league.html'
    success_url = reverse_lazy('league')


class DetailLeagueView(View):
    def get(self, request, id):
        league = League.objects.get(pk=id)
        season = league.season_set.order_by("-season")
        paginator = Paginator(season, 1)
        page = request.GET.get('page')
        seasons = paginator.get_page(page)
        teamss = Team.objects.filter(played_in_season__league=league)
        teams = []
        for team in teamss:
            if team not in teams:
                teams.append(team)
        return render(request, "detail_league.html", {'league': league, 'teams': teams, 'seasons':seasons})


class TeamView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, "team.html", {'objects': teams})


class AddTeamView(PermissionRequiredMixin, View):
    permission_required = 'footballscore_app.add_team'
    def get(self, request):
        form = TeamForm
        return render(request, "add_team.html", {'form': form})

    def post(self, request):
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teams')
        return render(request, "add_team.html", {'form': form})


class EditTeamView(View):
    def get(self, request, id):
        team = Team.objects.get(pk=id)
        form = TeamForm(instance=team)
        return render(request, "edit_team.html", {'form': form})

    def post(self, request, id):
        team = Team.objects.get(pk=id)
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect(f'/footballscore/teams/')
        return render(request, "edit_team.html", {'form': form})


class DeleteTeamView(DeleteView):
    model = Team
    template_name = 'delete_team.html'
    success_url = reverse_lazy('teams')

class DetailTeamView(View):
    def get(self, request, id):
        team = Team.objects.get(pk=id)
        season = team.played_in_season.order_by('-season')
        paginator = Paginator(season, 1)
        page = request.GET.get('page')
        seasons = paginator.get_page(page)
        matchess = Match.objects.all()
        matches = []
        for match in matchess:
            if match.team_home.team.name == team.name or match.team_away.team.name == team.name:
                matches.append(match)
        return render(request, "detail_team.html", {'team': team, 'matches': matches, 'seasons':seasons})


class AddMatchView(PermissionRequiredMixin, View):
    permission_required = 'footballscore_app.add_match'
    def get(self, request):
        form = MatchForm
        return render(request, "add_match.html", {'form': form})

    def post(self, request):
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, "add_match.html", {'form': form})
